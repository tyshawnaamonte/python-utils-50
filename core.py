import time
import random
from functools import wraps

def retry_network_operation(
    max_retries=3,
    initial_delay=1.0,
    backoff_factor=2.0,
    jitter=True,
    exceptions=(ConnectionError, TimeoutError, OSError)
):
    """Decorator for retrying network operations.
    Applies exponential backoff and optional random jitter.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            last_exception = None
            # Loop over attempts, including the initial one
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt == max_retries:
                        # No more retries left
                        break
                    # Add jitter to prevent synchronized retries
                    sleep_time = delay
                    if jitter:
                        sleep_time *= (0.5 + random.random())
                    time.sleep(sleep_time)
                    # Increase delay for next attempt
                    delay *= backoff_factor
            # After exhausting retries, propagate the exception
            raise last_exception
        return wrapper
    return decorator

# Example usage: decorate a function that performs network ops
@retry_network_operation(max_retries=4, initial_delay=0.1)
def example_network_call(payload):
    """Simulates a network operation that can fail intermittently."""
    # Simulate random failure for demonstration purposes
    if random.random() < 0.65:
        raise ConnectionError("Connection refused or timeout")
    return {"status": "success", "data": payload}