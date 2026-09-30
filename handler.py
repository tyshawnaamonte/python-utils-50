import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    """
    Decorator for retrying network operations with exponential backoff.
    
    :param exceptions: tuple of exceptions to catch
    :param tries: max number of attempts
    :param delay: initial delay between retries
    :param backoff: multiplier for delay
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt, current_delay = 1, delay
            while attempt <= tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(f'Operation failed after {tries} attempts')
                        raise
                    
                    logger.warning(f'Attempt {attempt} failed: {e}. Retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    attempt += 1
                    current_delay *= backoff
        return wrapper
    return decorator

# Example usage for network calls:
# @retry((ConnectionError, TimeoutError), tries=3)
# def fetch_data(url):
#     pass