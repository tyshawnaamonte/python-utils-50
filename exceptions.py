import functools
from typing import Any, Callable, TypeVar, ParamSpec

T = TypeVar('T')
P = ParamSpec('P')

class PerformanceError(Exception):
    """Custom exception for utility performance bottlenecks."""
    pass

def cache_result(func: Callable[P, T]) -> Callable[P, T]:
    """Thread-safe memoization decorator for compute-intensive tasks."""
    cache: dict[tuple[Any, ...], T] = {}

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_result
def validate_resource_intensity(data: str) -> bool:
    """Mock validation function with memoization optimization."""
    # Simulate expensive computation
    result = len(data.strip()) > 0
    return result

class ProcessingException(PerformanceError):
    """Standardized exception for processing failures."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(f"[{code}] {message}")
        self.code = code