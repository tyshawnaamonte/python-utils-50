import time
import functools
import logging

# Configure basic logger for utility output
logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=1.0, backoff=2):
    """
    Decorator to implement exponential backoff retry logic.
    Catches generic exceptions for network-related tasks.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2)
def fetch_data_from_source(url):
    """Example usage of the retry decorator."""
    # Simulating actual network call logic here
    logger.info(f"Fetching data from {url}")
    return {"status": "success", "url": url}