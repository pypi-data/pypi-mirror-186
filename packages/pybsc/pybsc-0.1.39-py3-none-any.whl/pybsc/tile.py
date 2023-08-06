import numpy as np


def squared_tile(n):
    if n < 1:
        raise ValueError('input n should be greater than 0.')
    tmp = int(np.ceil(np.sqrt(n)))
    if tmp * tmp == n:
        return (tmp, tmp)
    if tmp * (tmp - 1) >= n:
        return tmp, tmp - 1
    i = 0
    while tmp * (tmp - i) > n:
        i += 1
    return (tmp, tmp - i + 1)
