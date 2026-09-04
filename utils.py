import time
import functools
import random
from typing import Callable, Type, Tuple, Any

class MaxRetriesExceededError(Exception):
    """Exception raised when maximum retry attempts are reached."""
    pass

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True
) -> Callable:
    """
    Decorator to retry a function call with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        raise MaxRetriesExceededError(
                            f"Function '{func.__name__}' failed after {tries} attempts."
                        ) from e
                    
                    sleep_time = attempt_delay
                    if jitter:
                        sleep_time *= random.uniform(0.5, 1.5)
                    
                    time.sleep(sleep_time)
                    attempt_delay *= backoff
        return wrapper
    return decorator