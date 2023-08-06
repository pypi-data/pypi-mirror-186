import functools
import warnings

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn(f"Call to deprecated function {func.__name__}.",
                      category=DeprecationWarning,
                      stacklevel=2)
        return func(*args, **kwargs)
    return new_func
