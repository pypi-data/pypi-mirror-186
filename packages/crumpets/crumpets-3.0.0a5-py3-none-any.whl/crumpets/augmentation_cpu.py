import math
import numpy as np
import cv2


# don't use OpenCL
# prevents spawning GPU processes that hog memory
try:
    cv2.ocl.setUseOpenCL(False)
except AttributeError:
    pass
# run single-threaded; only warpAffine benefits and scales poorly
cv2.setNumThreads(1)


SIGMOID_RANGE = 6.279
SIGMOID_OFFSET = 1 / (1 + math.exp(SIGMOID_RANGE))
TANH_RANGE = 1 - 2 * SIGMOID_OFFSET
TANH_OFFSET = math.atanh(TANH_RANGE)


def _sigmoid(n, sigmoid, dtype=np.float32):
    if sigmoid:
        x = _make_base_lut(n, sigmoid=True, dtype=dtype) \
            * (-2 * SIGMOID_RANGE) + SIGMOID_RANGE
    else:
        x = np.linspace(SIGMOID_RANGE, -SIGMOID_RANGE, n, dtype=dtype)
    y = 1 / (1 + np.exp(x))
    y -= SIGMOID_OFFSET
    # add tiny offset, otherwise max = 1.0000000000000002
    y /= 1 - 2 * SIGMOID_OFFSET + 1e-16
    return y


def _arctanh(n, sigmoid, dtype=np.float32):
    if sigmoid:
        return np.linspace(0, 1, n, dtype=dtype)
    x = np.linspace(-TANH_RANGE, TANH_RANGE, n)
    y = np.arctanh(x)
    y += TANH_OFFSET
    y /= 2 * TANH_OFFSET
    return y


def _make_base_lut(n, sigmoid=False, dtype=np.float32):
    if sigmoid:
        return _sigmoid(n, False, dtype=dtype)
    else:
        return np.linspace(0, 1, n, dtype=dtype)


def _make_contrast_luts(n, sigmoid=False, dtype=np.float32):
    return (
               _sigmoid(n, sigmoid=sigmoid, dtype=dtype),
               _arctanh(n, sigmoid=sigmoid, dtype=dtype),
    )


DTYPE_INFO = {
    np.uint8: (
        np.int16,
        -np.iinfo(np.uint8).max-1,
        np.iinfo(np.uint8).max,
    ),
    np.uint16: (
        np.int32,
        -np.iinfo(np.uint16).max-1,
        np.iinfo(np.uint16).max,
    ),
    np.int16: (
        np.int16,
        0,
        2**15-1,
    )
}


DEFAULT_LUTS = (
    _make_base_lut(2 ** 12, sigmoid=True),
    *_make_contrast_luts(2 ** 12, sigmoid=True),
)
DTYPE_LUTS = {
    np.uint8: (
        _make_base_lut(2 ** 8, sigmoid=False),
        *_make_contrast_luts(2 ** 8, sigmoid=False),
    ),
    np.int64: (
        _make_base_lut(2 ** 12, dtype=np.float64, sigmoid=True),
        *_make_contrast_luts(2 ** 12, dtype=np.float64, sigmoid=True),
    ),
    np.uint64: (
        _make_base_lut(2 ** 12, dtype=np.float64, sigmoid=True),
        *_make_contrast_luts(2 ** 12, dtype=np.float64, sigmoid=True),
    ),
    np.float64: (
        _make_base_lut(2 ** 12, dtype=np.float64, sigmoid=True),
        *_make_contrast_luts(2 ** 12, dtype=np.float64, sigmoid=True),
    ),
}


def add_gamma(im, color, gamma_gray, gamma_color, contrast,
              _base_lut=None,
              _pos_contrast_lut=None,
              _neg_contrast_lut=None):
    """
    A Function that takes a numpy array that contains an Image and information about the desired gamma
    values and takes those gamma values to apply gamma correction to the images.

    :param im: the numpy array that contains the Image data
    :param color: flag that indicates if gamma_color should be used
    :param gamma_gray: gray parameter of the gamma correction
    :param gamma_color: color parameter of the gamma correction
    :param contrast: contrast parameter of the gamma correction
    :param _base_lut: a lookup table that can be precomputed. Defaults to None. None indicates that the default lookup
    table should be used. The default lookup table is computed only once and then cached.
    :param _pos_contrast_lut: similar to base_lut, just for the positive part of the contrast
    :param _neg_contrast_lut: see positive... contrast is treated asymmetrically to give better results
    """
    # noinspection PyTupleAssignmentBalance
    base_lut, pos_lut, neg_lut = DTYPE_LUTS.get(im.dtype.type, DEFAULT_LUTS)
    org_type = im.dtype.type
    temp_type = base_lut.dtype.type
    lut_size = len(base_lut)
    _, _, maxv = DTYPE_INFO[im.dtype.type]
    base_lut = _base_lut or base_lut
    pos_lut = _pos_contrast_lut or pos_lut
    neg_lut = _neg_contrast_lut or neg_lut

    # check inputs
    if not gamma_gray:
        gamma_gray = 1
    if not color or not gamma_color:
        gamma_color = (1,)
    if contrast is None:
        contrast = 0

    # make sure number of color gammas and channels match
    if len(im.shape) != 3:
        im = im[:, :, np.newaxis]
    nchannels = im.shape[2]
    ngammas = len(gamma_color)
    if nchannels != ngammas:
        if ngammas == 1:
            ngammas *= nchannels
            gamma_color = gamma_color * nchannels
        elif nchannels == 1:
            im = im.repeat(ngammas, 2)
        else:
            raise ValueError(
                'cannot broadcast %d channels and %d gamma_color values'
                % (nchannels, ngammas)
            )

    if org_type != np.uint8:
        # transform input with bigger dtypes into non-linear space
        im = im.astype(temp_type)
        im *= 2 * TANH_RANGE / maxv
        im -= TANH_RANGE
        np.clip(im, -TANH_RANGE, TANH_RANGE, out=im)
        np.arctanh(im, out=im)
        im += TANH_OFFSET
        im *= 1 / 2 / TANH_OFFSET  * (lut_size - 1)

    # create the contrast lookup table
    if contrast > 0:
        lut = (1 - contrast) * base_lut + contrast * pos_lut
    elif contrast < 0:
        lut = (1 + contrast) * base_lut - contrast * neg_lut
    else:
        lut = base_lut

    # add gamma for each channel and apply lookup table
    lower = im.astype(np.int64)
    upper = np.ceil(im).astype(np.int64)
    diff = upper.astype(temp_type)
    diff -= im
    for i, gamma in enumerate(gamma_color):
        clut = lut ** (gamma_gray * gamma) * maxv
        if org_type != np.uint8:
            low = clut.take(lower[:, :, i])
            low += diff[:, :, i] * (clut.take(upper[:, :, i]) - low)
            im[:, :, i] = low
        else:
            im[:, :, i] = clut.round().astype(org_type).take(im[:, :, i])
    if np.issubdtype(org_type, np.integer):
        np.around(im, out=im)

    return im.astype(org_type)


def add_noise_rgb(im, strength):
    """
    A Function that takes a numpy array that contains an Image and information about the desired rgb noise
    and takes those values to add noise to the images. This function adds rgb noise, that mimics the noise of a
    camera sensor, what means that green has less noise.

    :param im: the numpy array that contains the Image data
    :param strength: strength of the noise

    """
    h, w, c = im.shape
    size = int(h//2), int(w//2)
    target_size = h, w
    if c == 1:
        sizes = target_size,
    else:
        sizes = size, target_size, size
    target_sizes = (target_size,) * c
    strengths = [strength*r for r in [1.0, 0.5, 1.0]]
    cs = range(c)
    noise_type, minv, maxv = DTYPE_INFO[im.dtype.type]
    for i, size, target_size, s in zip(cs, sizes, target_sizes, strengths):
        noisy = np.random.randint(
            int(minv*s), int(maxv*s), size, dtype=noise_type
        )
        if size != target_size:
            # cv2.resize does not support int32
            if noise_type is np.int32:
                noisy = noisy.astype(np.float32)
            noisy = cv2.resize(noisy, target_size[::-1],
                               interpolation=cv2.INTER_LINEAR)
        noisy += im[:, :, i]
        np.clip(noisy, 0, maxv, im[:, :, i])
    if len(im.shape) != 3:
        im = im[:, :, np.newaxis]
    return im


def add_noise_other(im, strength):
    """
    A Function that takes a numpy array that contains an Image and information about the desired noise
    and takes those values to add noise to the images.

    :param im: the numpy array that contains the Image data
    :param strength: strength of the noise

    """
    noise_type, minv, maxv = DTYPE_INFO[im.dtype.type]
    noisy = np.random.randint(
        int(minv*strength), int(maxv*strength), im.shape, dtype=noise_type
    )
    noisy += im
    np.clip(noisy, 0, maxv, im)
    return im


def add_blur(im, sigma):
    """
    A Function that takes a numpy array that contains an Image and information about the desired blur
    and blurs the image. It uses cv2 to blur the image, for more information about the sigma parameter have a look into
    the cv2 documentation. cv.GaussianBlur

    :param im: the numpy array that contains the Image data
    :param sigma: the sigma of the gaussian blur

    """
    # sigma is relative to image width
    sigma *= im.shape[1]
    im = cv2.GaussianBlur(im, (0, 0), sigma)
    if len(im.shape) != 3:
        im = im[:, :, np.newaxis]
    return im
