import functools
from typing import Any, Callable, Dict

class ConfigCache:
    """Thread-safe memoized configuration access class."""
    _cache: Dict[str, Any] = {}

    @classmethod
    def get_setting(cls, key: str, default: Any = None) -> Any:
        """Retrieve setting with performance-oriented memoization."""
        if key not in cls._cache:
            cls._cache[key] = cls._load_from_source(key, default)
        return cls._cache[key]

    @staticmethod
    def _load_from_source(key: str, default: Any) -> Any:
        # Simulate high-latency file I/O or environment lookup
        import os
        return os.getenv(key, default)

    @classmethod
    def clear(cls):
        cls._cache.clear()

class LazyConfig:
    """Decorator for lazy property evaluation."""
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value

def memoize_config(func: Callable) -> Callable:
    """Performance optimization for function-based lookups."""
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper