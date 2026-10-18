import functools
import random
import time
from typing import Any, Callable, Tuple, Type


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff and jitter.

    :param max_retries: Maximum number of attempts before raising exception.
    :param initial_delay: Base delay in seconds before the first retry.
    :param backoff_factor: Multiplier for exponential backoff delay.
    :param jitter: Add random variance to delay to avoid synchronized retries.
    :param retryable_exceptions: Tuple of exceptions that trigger a retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        raise exc
                    
                    sleep_duration = delay
                    if jitter:
                        sleep_duration += random.uniform(0, 0.1 * delay)
                    
                    time.sleep(sleep_duration)
                    delay *= backoff_factor

        return wrapper
    return decorator