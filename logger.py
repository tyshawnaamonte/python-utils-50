import logging
import functools
from typing import Callable, Any

# global cache for loggers to avoid redundant instantiation
_loggers = {}

def get_logger(name: str) -> logging.Logger:
    """Thread-safe singleton access to named loggers."""
    if name not in _loggers:
        _loggers[name] = logging.getLogger(name)
    return _loggers[name]

def lazy_log_execution(func: Callable) -> Callable:
    """Decorator to log function execution time lazily."""
    logger = get_logger(func.__module__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not logger.isEnabledFor(logging.DEBUG):
            return func(*args, **kwargs)
        
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f"function {func.__name__} executed in {duration:.4f}s")
        return result
    return wrapper

class PerformanceLogger:
    """Batch-oriented logging handler for high throughput."""
    def __init__(self, logger_name: str = "perf_logger"):
        self.logger = get_logger(logger_name)
        self._buffer = []

    def emit(self, message: str, flush_threshold: int = 10) -> None:
        """Buffered logging to minimize I/O overhead."""
        self._buffer.append(message)
        if len(self._buffer) >= flush_threshold:
            self.flush()

    def flush(self) -> None:
        """Flush buffered logs to standard output."""
        if self._buffer:
            self.logger.info(" | ".join(self._buffer))
            self._buffer.clear()