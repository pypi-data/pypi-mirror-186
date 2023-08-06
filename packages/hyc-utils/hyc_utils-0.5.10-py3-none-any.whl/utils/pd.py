import functools

import numpy as np
import torch

def _formatter(x, float_format=None, verbose=False):
    if isinstance(x, np.ndarray):
        if verbose:
            return f"np.ndarray {x.shape} ({x.dtype})"
        return f"{x.shape}"
    if isinstance(x, torch.Tensor):
        if verbose:
            return f"torch.Tensor {tuple(x.shape)} ({x.dtype})"
        return f"{tuple(x.shape)}"
    if isinstance(x, tuple):
        if verbose:
            return f"tuple ({len(x)}) {tuple([type(e).__name__ for e in x])}"
        return f"tuple ({len(x)})"
    if isinstance(x, list):
        if verbose:
            return f"list ({len(x)}) {[type(e).__name__ for e in x]}"
        return f"list ({len(x)})"
    if isinstance(x, dict):
        if verbose:
            d = {k: type(v).__name__ for k, v in x.items()}
            return f"dict ({len(x)}) {d}"
        return f"dict ({len(x)})"
    if isinstance(x, np.floating):
        if float_format is None:
            return f'{x:.4f}'
        return float_format(x)
    return str(x)

def display(df, float_format=None, verbose=False, **kwargs):
    default_kwargs = {
        'max_rows': 6,
        'show_dimensions': True,
        'formatters': {k: functools.partial(_formatter, float_format=float_format, verbose=verbose) for k in df.columns},
    }
    default_kwargs.update(kwargs)

    try:
        get_ipython
        from IPython.display import display as ipy_display
        from IPython.core.display import HTML
    except:
        raise RuntimeError("display only works in jupyter notebook")
        
    ipy_display(HTML(df.to_html(**default_kwargs)))