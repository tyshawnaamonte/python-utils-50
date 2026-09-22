import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results
_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for memory-efficient chunked list processing."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for simple execution time logging."""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[PERF] {self.name} took {elapsed:.4f} seconds")

def clear_cache() -> None:
    """Manual memory management for function caches."""
    _CACHE.clear()