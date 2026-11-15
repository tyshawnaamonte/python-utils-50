import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)): 
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def fetch_data_from_network(url):
    """Simulated network fetch operation."""
    # Implementation logic for network request would go here
    pass