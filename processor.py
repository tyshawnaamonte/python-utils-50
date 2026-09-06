import functools
from typing import Callable, Any, Dict

# Cache for compute-intensive transformations
_memoization_cache: Dict[tuple, Any] = {}

def lru_cache_processor(maxsize: int = 128) -> Callable:
    """Decorator to optimize recurring data processing tasks."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key in _memoization_cache:
                return _memoization_cache[key]
            
            result = func(*args, **kwargs)
            if len(_memoization_cache) >= maxsize:
                _memoization_cache.pop(next(iter(_memoization_cache)))
            
            _memoization_cache[key] = result
            return result
        return wrapper
    return decorator

@lru_cache_processor(maxsize=256)
def process_heavy_data(data_chunk: str, complexity: int) -> str:
    """Simulates heavy computation with linear reduction."""
    result = "".join(sorted(data_chunk)) * complexity
    return result[:100]

def clear_processor_cache() -> None:
    """Manual memory management for processor cache."""
    _memoization_cache.clear()