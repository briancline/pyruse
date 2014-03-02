from functools import wraps


def cacheable(f):
    @wraps(f)
    def wrapper(*a, **kwa):
        if not hasattr(f, '__cache__'):
            f.__cache__ = f(*a, **kwa)
        return f.__cache__

    return wrapper


def is_release(x):
    return ('a' not in x and
            'b' not in x and
            'c' not in x and
            'rc' not in x)  # slightly redundant after previous expression
