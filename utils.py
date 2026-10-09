import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
) -> Callable:
    """
    Decorator that retries a function call on specified exceptions with exponential backoff.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            curr_delay = delay
            for attempt in range(1, retries + 2):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt > retries:
                        logger.error(f"Function {func.__name__} failed after {retries} retries.")
                        raise e
                    logger.warning(
                        f"Exception '{e}' caught. Retrying {func.__name__} "
                        f"in {curr_delay:.2f} seconds (Attempt {attempt}/{retries})..."
                    )
                    time.sleep(curr_delay)
                    curr_delay *= backoff
        return wrapper
    return decorator
