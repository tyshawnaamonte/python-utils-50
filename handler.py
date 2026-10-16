import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: Tuple[Type[Exception], ...], retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on specific errors."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure((ConnectionError, TimeoutError), retries=3, delay=2.0)
def fetch_data(url: str):
    """Example network call handler."""
    # Implementation would typically use requests or httpx
    logger.info(f"Fetching data from {url}")
    return {"status": "success"}