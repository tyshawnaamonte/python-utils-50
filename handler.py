import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

class NetworkHandler:
    """Handles network-bound operations with integrated retry logic."""
    
    def __init__(self, timeout=5):
        self.timeout = timeout

    @retry_network_op(max_retries=3, delay=2.0)
    def execute_request(self, url):
        """Mock method representing a network request."""
        logger.info(f"Executing request to {url}")
        # In a real scenario, use requests.get() here
        return {"status": 200, "url": url}