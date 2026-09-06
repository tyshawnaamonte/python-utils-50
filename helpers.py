import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, batch_size: int = 100) -> list:
    """Generator for chunking large lists to reduce memory overhead."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator for monitoring execution performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Execution of {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Manual invalidation of the internal memory cache."""
    global _CACHE
    _CACHE.clear()