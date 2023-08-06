from torch import device


def is_single_torch_device(val):
    """checks if val is a value determining a single cuda device"""
    try:
        device(val)
        return True
    except TypeError:
        return False


def is_cpu_only(val):
    """checks if val is a value determining cpu-only cuda devices"""
    try:
        try:
            res = device(val).type == 'cpu'
        except TypeError:
            res = all([device(d).type == 'cpu' for d in val])
        return res
    except TypeError:
        raise TypeError('Given value {} is neither iterable nor a torch device!'.format(val))
