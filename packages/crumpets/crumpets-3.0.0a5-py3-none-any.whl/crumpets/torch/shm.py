import multiprocessing as mp

import numpy as np
import torch
from msgpack import unpackb
from msgpack_numpy import decode as _decode_numpy

from ..shm import DummyBufferManager
from ..shm import SharedBufferManager


__all__ = [
    'shared_tensor',
    'DummyTensorManager',
    'SharedTensorManager',
]


def shared_tensor(shape, dtype=np.float32, device_type='cuda'):
    """
    Create a torch tensor that resides in shared memory.

    :param shape:
        array shape
    :param dtype:
        numpy dtype
    :param device_type:
        tensor.pin_memory() if 'cuda'
    :return: np.ndarray
    """
    try:
        dtype = np.dtype(dtype)
        dtype = torch.from_numpy(np.empty(1, dtype=dtype)).dtype
    except TypeError:
        pass
    tensor = torch.empty(shape, dtype=dtype)
    tensor.share_memory_()
    if device_type == 'cuda':
        tensor = tensor.pin_memory()
    return tensor


EXT_SHARED = ord('s')


class DummyTensorManager(DummyBufferManager):
    """
    Torch replacement for DummyBufferManager.
    Returns torch tensors instead of numpy arrays when unpacking.

    :param device:
        output device; buffers are copied here when ready
    """
    def __init__(self, device='cuda:0'):
        DummyBufferManager.__init__(self)
        self.device = torch.device(device)

    def next(self):
        raise NotImplementedError('DummyTensorManager does not support next')

    def _decode_torch(self, obj):
        obj = _decode_numpy(obj)
        if isinstance(obj, np.ndarray):
            return torch.from_numpy(obj).to(self.device)
        return obj

    def unpack(self, data):
        return unpackb(data, object_hook=self._decode_torch, raw=False)


class SharedTensorManager(SharedBufferManager):
    def __init__(self, num_buffers, batch_size, buffer_specs,
                 device='cuda:0', _queueclass=mp.Queue):
        self.device = torch.device(device)
        SharedBufferManager.__init__(self, num_buffers, batch_size,
                                     buffer_specs, _queueclass)

    def _create_buffers(self):
        return [
            {k: (i, spec, shared_tensor(spec[0], spec[1], self.device.type))
             for k, spec in self.buffer_specs.items()}
            for i in range(self.num_buffers)
        ]

    def _create_alias_decode(self, obj):
        return obj.view(obj.size()).to(self.device)

    @staticmethod
    def _create_alias_next(obj):
        return obj.numpy()
