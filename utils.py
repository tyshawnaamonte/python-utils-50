import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=2, backoff=2):
    """Decorator for retrying functions on exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts")
                        raise e
                    
                    logger.warning(f"Retry {attempts}/{max_attempts} due to {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator