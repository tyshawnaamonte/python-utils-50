import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = (
        TimeoutError,
        ConnectionError,
        OSError,
    ),
    jitter: bool = True,
) -> Callable:
    """Decorator to retry network operations with exponential backoff and jitter."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    retries += 1
                    if retries > max_retries:
                        logger.error(
                            "Operation %s failed after %d retries: %s",
                            func.__name__,
                            max_retries,
                            exc,
                        )
                        raise exc

                    sleep_time = backoff_factor * (2 ** (retries - 1))
                    if jitter:
                        sleep_time += random.uniform(0, 0.1 * sleep_time)

                    logger.warning(
                        "Attempt %d/%d failed for %s: %s. Retrying in %.2fs...",
                        retries,
                        max_retries,
                        func.__name__,
                        exc,
                        sleep_time,
                    )
                    time.sleep(sleep_time)

        return wrapper

    return decorator
