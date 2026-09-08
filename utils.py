import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
          retries: int = 3, 
          delay: float = 1.0) -> Callable:
    """Decorator for retrying functions on specific exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(exceptions=(ConnectionError,), retries=3, delay=2.0)
def fetch_data(url: str) -> str:
    """Example network operation function."""
    # Simulating a network request
    print(f"Fetching from {url}...")
    raise ConnectionError("Network request failed")