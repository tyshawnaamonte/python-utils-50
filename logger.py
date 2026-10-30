import logging
import functools
from typing import Callable, Any

# Configure a shared high-performance logger
logger = logging.getLogger('python-utils-50')

_cache = {}

def memoized_logger(func: Callable) -> Callable:
    """
    Decorator to cache logger initialization and reduce overhead.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

@memoized_logger
def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a logger instance with standardized formatting.
    """
    instance = logging.getLogger(name)
    if not instance.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        instance.addHandler(handler)
        instance.setLevel(logging.INFO)
    return instance

def log_execution_time(func: Callable) -> Callable:
    """
    Wrapper to track and log execution time.
    """
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f"Function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper