from collections import OrderedDict
from functools import wraps

_MISSING = object()


def _normalize(obj):
    """Turn common containers into a canonical, hashable form."""
    if isinstance(obj, (list, tuple)):
        # lists and tuples with equal elements share a key
        return ("seq", tuple(_normalize(x) for x in obj))
    if isinstance(obj, dict):
        # frozenset makes the key independent of insertion order
        return ("dict", frozenset((_normalize(k), _normalize(v)) for k, v in obj.items()))
    if isinstance(obj, (set, frozenset)):
        return ("set", frozenset(_normalize(x) for x in obj))
    return obj


def lru_memoize(capacity):
    def decorator(func):
        cache = OrderedDict()  # key -> value, ordered least to most recently used

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (
                tuple(_normalize(a) for a in args),
                frozenset((name, _normalize(v)) for name, v in kwargs.items()),
            )

            value = cache.get(key, _MISSING)
            if value is not _MISSING:
                cache.move_to_end(key)       # hit counts as a use
                return value

            value = func(*args, **kwargs)    # miss: compute (exceptions are not cached)
            if capacity > 0:
                cache[key] = value
                cache.move_to_end(key)       # insertion counts as a use
                while len(cache) > capacity:
                    cache.popitem(last=False)  # evict least recently used
            return value

        wrapper.cache = cache
        return wrapper

    return decorator