import math
import warnings

import numpy as np
import cv2
import torch
import torch.nn.functional as F

from ..augmentation_cpu import _make_base_lut
from ..augmentation_cpu import _make_contrast_luts
from ..augmentation_cpu import TANH_RANGE
from ..augmentation_cpu import TANH_OFFSET


# don't use OpenCL
# prevents spawning GPU processes that hog memory
try:
    cv2.ocl.setUseOpenCL(False)
except AttributeError:
    pass
# run single-threaded; only warpAffine benefits and scales poorly
cv2.setNumThreads(1)


DTYPE_INFO = {
    'torch.ByteTensor': (
        torch.float32,
        float(-2 ** 8),
        float(2 ** 8 - 1),
    ),
    'torch.cuda.ByteTensor': (
        torch.float32,
        float(-2 ** 8),
        float(2 ** 8 - 1),
    ),
    'torch.ShortTensor': (
        torch.float32,
        float(-2 ** 15),
        float(2 ** 15 - 1),
    ),
    'torch.cuda.ShortTensor': (
        torch.float32,
        float(-2 ** 15),
        float(2 ** 15 - 1),
    ),
    'torch.cuda.FloatTensor': (
        torch.float32,
        -1.0,
        1.0
    ),
    'torch.cuda.DoubleTensor': (
        torch.float64,
        -1.0,
        1.0
    ),
    'torch.cuda.HalfTensor': (
        torch.float32,
        -1.0,
        1.0
    ),
    'torch.FloatTensor': (
        torch.float32,
        -1.0,
        1.0
    ),
    'torch.DoubleTensor': (
        torch.float64,
        -1.0,
        1.0
    ),
    'torch.HalfTensor': (
        torch.float16,
        -1.0,
        1.0
    ),
    'torch.cuda.IntTensor': (
        torch.float32,
        float(-np.iinfo(np.uint32).max - 1),
        float(2 ** 31 - 1)
    ),
    'torch.IntTensor': (
        torch.float32,
        -np.iinfo(np.uint32).max - 1,
        float(2 ** 31 - 1)
    )
}


DEFAULT_LUTS = (
    _make_base_lut(2 ** 12, sigmoid=True),
    *_make_contrast_luts(2 ** 12, sigmoid=True),
)
DTYPE_LUTS = {
    torch.uint8: (
        _make_base_lut(2 ** 8, sigmoid=False),
        *_make_contrast_luts(2 ** 8, sigmoid=False),
    ),
    torch.int64: (
        _make_base_lut(2 ** 12, dtype=np.float64, sigmoid=True),
        *_make_contrast_luts(2 ** 12, dtype=np.float64, sigmoid=True),
    ),
    torch.float64: (
        _make_base_lut(2 ** 12, dtype=np.float64, sigmoid=True),
        *_make_contrast_luts(2 ** 12, dtype=np.float64, sigmoid=True),
    ),
}


def __add_gamma_impl(
        im_tensor,
        augs,
        maxv,
        org_type,
        temp_type,
        lut_size,
        base_lut,
        positive_contrast_lut,
        negative_contrast_lut,
):
    device = im_tensor.device
    num_images, num_channels, h, w = im_tensor.shape
    # create the lookup tables over channels and apply augmentations
    luts = []
    for a in augs:
        # compute the combined gamma = gray * color
        color = a.get('color', True)
        gamma_gray = a.get('gamma_gray')
        gamma_gray = gamma_gray if gamma_gray is not None else 1
        gamma_color = a.get('gamma_color')
        if not color or not gamma_color:
            gamma_color = num_channels * [1]
        if len(gamma_color) == 1:
            gamma_color *= num_channels
        elif len(gamma_color) != num_channels:
            raise ValueError(
                'number of gamma_color values must be broadcastable to number of channels'
            )

        # create the lookup tables
        contrast = a.get('contrast', 0)
        if contrast > 0:
            lut = (1 - contrast) * base_lut + contrast * positive_contrast_lut
        elif contrast < 0:
            lut = (1 + contrast) * base_lut - contrast * negative_contrast_lut
        else:
            lut = base_lut
        for gamma in gamma_color:
            luts.append(lut ** (gamma_gray * gamma) * maxv)

    # put lookup tables on GPU
    lut = torch.tensor(luts, dtype=temp_type, device=device).reshape(-1)
    # view im_tensor as shape [num_images*num_channels, h, w]
    # offset the values in each row so they point to the next lookup table:
    # row_0 = row_0 + 0 * lut_values
    # row_1 = row_1 + 1 * lut_values
    # row_2 = row_2 + 2 * lut_values
    # ...
    # row_n = row_n + n * lut_values
    offset = torch.arange(num_images*num_channels, dtype=im_tensor.dtype)
    offset = (offset * lut_size).reshape(num_images*num_channels, 1).to(device)
    im_tensor = im_tensor.reshape(num_images*num_channels, -1)
    im_tensor += offset
    # apply lookup table
    if org_type == torch.uint8:
        # take fast path for uint8, round for better accuracy
        im_tensor[...] = lut.round_().to(org_type).take(
            im_tensor  # .to(torch.int64)
        )
    else:
        # other types need linear interpolation
        lower = im_tensor.to(torch.int64)
        upper = im_tensor.ceil().to(torch.int64)
        diff = upper.to(temp_type)
        diff -= im_tensor
        im_tensor[...] = lut.take(lower)
        im_tensor.lerp_(lut.take(upper), diff)
        if not org_type.is_floating_point:
            # round for integer types for better accuracy
            im_tensor.round_()


def add_gamma(
        im_tensor,
        augs,
        maxv=None
):
    """
    A Function that takes a tensor that contains a Batch of Images
    and a list of dictionaries that contain information about the
    desired gamma values and takes those gamma values to apply
    gamma correction to the images.
    This function is hardware accelerated, so be sure that the
    im_tensor is located on the GPU.

    :param im_tensor: the Tensor that contains the Image data
    :param augs: a list of dictionaries.
                 Each dict should contain a 'color', a 'gamma_gray',
                 a 'gamma_color', and a 'contrast' value to specify
                 the behaviour of the gamma augmentation.
                 For further information see
                 :func:`~crumpets.augmentation.randomize_image`
    :param maxv: Maximum value of the entries.
                 This value is data type dependent, so be careful with it.
                 It defaults to "None".
                 None indicates that the value is taken according to
                 the data type of the tensor.
    """
    if not im_tensor.is_cuda:
        warnings.warn("input should be cuda tensor")

    im_tensor = im_tensor.clone()
    # tensor needs to be contiguous for take function
    # im_tensor = im_tensor.contiguous()

    org_type = im_tensor.dtype
    temp_type, _, maxv_ = DTYPE_INFO[im_tensor.type()]
    maxv = maxv or maxv_

    base_lut, positive_contrast_lut, negative_contrast_lut = \
        DTYPE_LUTS.get(org_type, DEFAULT_LUTS)
    lut_size = len(base_lut)
    num_images = im_tensor.shape[0]
    num_channels = im_tensor.shape[1]
    if org_type == torch.uint8:
        # uint8 tensors can use int type for better efficiency
        im_tensor = im_tensor.to(torch.int64)
        # batch size can be pretty damn big
        batch_size = int((2 ** 63 - 1 - maxv) // num_channels)
    else:
        # transform input with bigger dtypes into non-linear space
        im_tensor = im_tensor.to(temp_type)
        # im_tensor *= 2 * TANH_RANGE / maxv
        # im_tensor -= TANH_RANGE
        im_tensor = torch.add(-TANH_RANGE, im_tensor, alpha=2 * TANH_RANGE / maxv)
        im_tensor.clamp_(-TANH_RANGE, TANH_RANGE)
        im_tensor.atanh_()
        # im_tensor *= 1 / 2 / TANH_OFFSET * (lut_size - 1)
        # im_tensor += 0.5 * (lut_size - 1)
        im_tensor = torch.add(0.5 * (lut_size - 1), im_tensor, alpha=1 / 2 / TANH_OFFSET * (lut_size - 1))
        # floating point types nee to use smaller batches to keep precision
        if org_type.is_floating_point:
            batch_size = int(192 // num_channels)
        else:
            batch_size = int((2 ** 24 - 1 - maxv) // num_channels)
    # process in batches to prevent index offset exceeding
    # precision of temp_type like float32
    for i in range(0, num_images, batch_size):
        __add_gamma_impl(
            im_tensor[i:i+batch_size],
            augs,
            maxv,
            org_type,
            temp_type,
            lut_size,
            base_lut,
            positive_contrast_lut,
            negative_contrast_lut,
        )
    return im_tensor.to(org_type)


def add_noise_rgb(im, augs, minv=None, maxv=None, internal_ftype=None):
    """
    A Function that takes a tensor that contains a batch of images
    and a list of dictionaries that contain information about the
    desired noise and takes this information to add noise according
    to the that to the images.

    This noise function tries to mimic the rgb noise of a camera
    sensor, what means that the green value has a lower noise.

    This function is hardware accelerated, so be sure that the im
    is located on the GPU.

    :param im: the Tensor that contains the Image data
    :param augs: a list of dictionaries.
                 Each dict should contain a 'noise' value to specify
                 the behaviour of the noise augmentation.
                 For further information see
                 :func:`~crumpets.augmentation.randomize_image`
    :param minv: Minimum value of the entries.
                 This value is data type dependent, so be careful with it.
                 It defaults to "None".
                 None indicates that the value is taken according
                 to the data type of the tensor.
    :param maxv: Maximum value of the entries.
                 This value is data type dependent, so be careful with it.
                 It defaults to "None".
                 None indicates that the value is taken according
                 to the data type of the tensor.
    :param internal_ftype: The type that is used internally to
                           compute the noise.
                           The type defaults to None, what indicates
                           that a fitting type is chosen according to
                           the input type.
                           For most types the internal type is float32.
    """
    if not im.is_cuda:
        warnings.warn("input should be cuda tensor")

    n, c, h, w = im.shape
    noise_type, minv1, maxv1 = DTYPE_INFO[im.type()]
    noise_type = internal_ftype if internal_ftype else noise_type
    minv = minv if minv else minv1
    maxv = maxv if maxv else maxv1
    strengths = [a['noise'] if 'noise' in a else 0 for a in augs]
    old_im_type = im.dtype
    im = im.type(noise_type)
    s = torch.from_numpy(np.asarray(strengths)[:, None, None, None]).to(noise_type).to(im.device)
    multiplier = torch.tensor([1, 0.5] + [1] * (c - 2), device=im.device, dtype=noise_type)
    # print(s.shape)
    # print(multiplier.shape)
    s = torch.mm(s.reshape(-1, 1), multiplier.reshape(1, -1)).reshape(n, c, 1, 1)
    noisyrb = torch.empty(n, c - 1, h, w, dtype=noise_type, device=im.device).uniform_(minv, maxv).to(im.device)
    noisyg = torch.empty(n, 1, h // 2, w // 2, dtype=noise_type, device=im.device).uniform_(minv, maxv).to(im.device)
    noisyg = torch.nn.functional.interpolate(input=noisyg, size=(h, w), mode="bilinear", align_corners=True)

    # print(noisyrb[:,0].reshape(n,1,h,w).shape)
    # print(noisyg.shape)
    # print(noisyrb[:,1:].reshape(n,c-2,h,w).shape)

    noisy = torch.cat([
        noisyrb[:, 0].reshape(n, 1, h, w),
        noisyg,
        noisyrb[:, 1:].reshape(n, c - 2, h, w)
    ], dim=1)

    noisy = torch.addcmul(im, 1, s, noisy.reshape(n, c, h, w))
    im = noisy.clamp(0, maxv).type(old_im_type)
    return im


def add_noise_other(im, augs, minv=None, maxv=None, internal_ftype=None):
    """
    A Function that takes a tensor that contains a batch of images
    and a list of dictionaries that contain information about the
    desired noise and adds noise according to that to the images.

    This function is Hardware accelerated, so be sure that the im
    tensor is located on the GPU.

    :param im: the Tensor that contains the image data
    :param augs: a list of dictionaries.
                 Each dict should contain a 'noise' value to specify
                 the behaviour of the noise augmentation.
                 For further information see
                 :func:`~crumpets.augmentation.randomize_image`
    :param minv: Minimum value of the entries.
                 This value is data type dependent, so be careful with it.
                 It defaults to "None".
                 None indicates that the value is taken according
                 to the data type of the tensor.
    :param maxv: Maximum value of the entries.
                 This value is data type dependent, so be careful with it.
                 It defaults to "None".
                 None indicates that the value is taken according
                 to the data type of the tensor.
    :param internal_ftype: The type that is used internally to
                           compute the noise.
                           For most types the internal type is float32.
                           The type defaults to None, what indicates
                           that a fitting type is chosen according
                           to the input type.
    """
    if not im.is_cuda:
        warnings.warn("input should be cuda tensor")

    n, c, h, w = im.shape
    noise_type, minv1, maxv1 = DTYPE_INFO[im.type()]
    noise_type = internal_ftype if internal_ftype else noise_type
    minv = minv if minv else minv1
    maxv = maxv if maxv else maxv1
    strengths = [a['noise'] if 'noise' in a else 0 for a in augs]
    old_im_type = im.dtype
    im = im.type(noise_type)
    s = torch.from_numpy(np.asarray(strengths)[:, None, None, None]).to(noise_type).to(im.device)
    noisy = torch.empty(n, c, h, w, dtype=noise_type, device=im.device).uniform_(minv, maxv).to(im.device)
    noisy = torch.addcmul(im, 1, s, noisy)
    im = noisy.clamp(minv, maxv).type(old_im_type)
    return im


def add_blur(im, augs):
    """
    A Function that takes a tensor that contains a batch of images
    and a list of dictionaries that contain information about the
    desired blur and takes this information to blur the image.

    This function is hardware accelerated, so be sure that the im
    is located on the GPU.

    :param im: the Tensor that contains the image data
    :param augs: a list of dictionaries.
                 Each dict should contain a 'blur' value.
                 This blur indicates the sigma value of the normal
                 distribution filter that is used to blur the image.
                 Also note that the blur value should be relative to
                 the image size, to achieve the same optical blur
                 effect on different image sizes.
                 For further information see
                 :func:`~crumpets.augmentation.randomize_image`
    """
    if not im.is_cuda:
        warnings.warn("input should be cuda tensor")

    n, c, h, w = im.shape
    threshold = 0.0  # 0.1 / 448
    # extract relevant augmentation
    imtype = im.type()

    if type(augs) is not list:
        raise Exception("Augmentations should be a list")
    if n != len(augs):
        raise Exception(
            "the number of augmentations should match the batch size, expected: " + str(n) + " but got " + str(
                len(augs)) + " \naugmentations: " + str(augs))
    sigmas = np.asarray([a['blur'] if 'blur' in a and a['blur'] > threshold else 0.0 for a in augs])

    if not any(sigmas):
        return im
    # sigma is relative to image width
    sigmas *= im.shape[3]
    # prepare kernels
    ksizes = [int(s * 6.6 - 2.3) | 1 if s >= 0.2 else 0 for s in sigmas]  # for roughly s <= 0.2 ksize would be < 0
    ksizes = [k if k >= 3 else 3 for k in ksizes]

    maxsize = max(ksizes)
    sigmas = [sigma or 1e-8 for sigma in sigmas]
    kernels = [cv2.getGaussianKernel(maxsize, sigma) for ksize, sigma in zip(ksizes, sigmas)]
    kernels = [torch.from_numpy(k.astype(np.float32)).repeat(c, 1, 1)
               for k in kernels if k is not None and k.size > 1]
    kernels = torch.stack(kernels)

    kernels = kernels.reshape(-1, 1, maxsize, 1).to(im.device)
    im = F.pad(im.float(), (0, 0, math.floor(maxsize / 2), math.floor(maxsize / 2)), mode='replicate')
    _, _, newh, neww = im.shape
    im = im.reshape(1, -1, newh, neww)
    im = F.conv2d(im, kernels, groups=n * c)
    im = F.pad(im.float(), (math.floor(maxsize / 2), math.floor(maxsize / 2), 0, 0), mode='replicate')
    _, _, newh, neww = im.shape
    im = im.reshape(1, -1, newh, neww)
    im = F.conv2d(im, kernels.reshape(-1, 1, 1, maxsize), groups=n * c)
    im = im.type(imtype).reshape(n, c, h, w)

    return im
