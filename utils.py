import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1..0, backoff=2.0, exceptions=(Exception,)):
    """Retry decorator for network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Failed {func.__name__} after {max_attempts} attempts: {e}")
                        raise
                    
                    logger.warning(f"Retrying {func.__name__} (attempt {attempt}/{max_attempts}) in {current_delay}s due to: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def safe_request(url, requests_func, *args, **kwargs):
    """Helper to execute an HTTP request safely with retry logic built-in."""
    @retry(max_attempts=3, delay=0.5, backoff=2.0)
    
    def _execute():
        response = requests_func(url, *args, **kwargs)
        response.raise_for_status()
        return response
        
    return _execute()
