import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (Exception,),
) -> Callable:
    """Decorator that retries a network operation with exponential backoff.

    :param max_retries: Maximum number of retry attempts allowed.
    :param initial_delay: Delay in seconds before the first retry.
    :param backoff_factor: Multiplier applied to delay after each failure.
    :param jitter: Adds random variance to delay to prevent thundering herd.
    :param exceptions: Exception types to intercept and trigger retries.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 2):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt > max_retries:
                        logger.error(
                            "Operation '%s' failed after %d retries. Exception: %s",
                            func.__name__,
                            max_retries,
                            err,
                        )
                        raise err

                    sleep_time = delay * (random.uniform(0.8, 1.2) if jitter else 1.0)
                    logger.warning(
                        "Attempt %d/%d for '%s' failed: %s. Retrying in %.2fs...",
                        attempt,
                        max_retries,
                        func.__name__,
                        err,
                        sleep_time,
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper
    return decorator
