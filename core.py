import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

# Decorator for performance measurement

def performance_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        duration = end_time - start_time  
        logger.info(f'Function {func.__name__} executed in {duration:.4f} seconds')
        return result
    return wrapper

class DataProcessor:
    def __init__(self, data):
        self.data = data

    @performance_logger
    def process_data(self):
        # Simulate a processing task
        time.sleep(2)  # Replace with actual data processing
        return [d * 2 for d in self.data]  

# Example usage
if __name__ == '__main__':
    processor = DataProcessor([1, 2, 3, 4, 5])
    processed_data = processor.process_data()
    print(processed_data)  
