import numpy as np

__all__ = [
    'isconst',
]

def isconst(x, axis=None, **kwargs):
    if axis is None:
        x = x.reshape(-1)
    else:
        if isinstance(axis, int):
            axis = [axis]
        axis = sorted([d % x.ndim for d in axis])[::-1]
        for d in axis:
            x = np.moveaxis(x, d,-1)
        x = x.reshape(*x.shape[:-len(axis)],-1)
        
    return np.isclose(x[...,:-1], x[...,1:], **kwargs).all(axis=-1)