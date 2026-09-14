import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries:
                        logger.error(f"Final attempt {attempt} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1)
def fetch_data(url):
    """Example function performing a network call."""
    # Simulating a network operation
    logger.info(f"Fetching data from {url}")
    # raise ConnectionError("Network unreachable") 
    return {"status": "success"}