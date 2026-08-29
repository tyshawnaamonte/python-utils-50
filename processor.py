import time
import random
from typing import Callable, Any

class RetryProcessor:
    """Handles retry logic for network operations with exponential backoff."""

    def __init__(self, max_retries: int = 3, initial_delay: float = 1.0, backoff_factor: float = 2.0):
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.backoff_factor = backoff_factor

    def execute(self, func: Callable[[], Any], *args, **kwargs) -> Any:
        """Execute a function with retry logic. Suitable for network calls."""
        delay = self.initial_delay
        last_exception = None
        for attempt in range(1, self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt == self.max_retries:
                    break
                # Add jitter to prevent thundering herd
                jitter = random.uniform(0, 0.1) * delay
                sleep_time = delay + jitter
                print(f"Retry attempt {attempt} failed: {e}. Sleeping for {sleep_time:.2f}s")
                time.sleep(sleep_time)
                delay *= self.backoff_factor
        raise ConnectionError(f"Network operation failed after {self.max_retries} attempts") from last_exception

# Demo function to simulate network operation
def simulated_network_call(fail_first_n: int = 2) -> str:
    """Simulates a flaky network request."""
    # Use a simple counter simulation
    if not hasattr(simulated_network_call, 'call_count'):
        simulated_network_call.call_count = 0
    simulated_network_call.call_count += 1
    if simulated_network_call.call_count <= fail_first_n:
        raise ConnectionError("Temporary network issue")
    return "Data fetched successfully"

if __name__ == "__main__":
    processor = RetryProcessor(max_retries=4, initial_delay=0.2, backoff_factor=1.5)
    try:
        result = processor.execute(simulated_network_call, fail_first_n=2)
        print(result)
    except Exception as e:
        print(str(e))