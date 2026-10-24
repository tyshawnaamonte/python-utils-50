import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_network_op(exceptions: tuple[Type[Exception], ...], 
                     max_retries: int = 3, 
                     delay: float = 1.0) -> Callable:
    """Decorator for retrying network-based operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= 2
                    else:
                        logger.error(f"Max retries reached. Final error: {e}")
            
            if last_exception:
                raise last_exception
        return wrapper
    return decorator