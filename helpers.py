import functools
import time
from typing import Callable, Any, Dict

_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator to yield chunks for memory-efficient processing."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def timing_decorator(func: Callable) -> Callable:
    """Utility for measuring function execution latency."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"DEBUG: {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Manual memory reclamation for the internal cache."""
    _CACHE.clear()