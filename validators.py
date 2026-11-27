import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input_data(data):
    """Ensures input data conforms to expected processing schema."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    required_keys = ['task_id', 'payload']
    for key in required_keys:
        if key not in data:
            raise KeyError(f"Missing required field: {key}")
            
    if not isinstance(data['task_id'], int) or data['task_id'] <= 0:
        raise ValueError("task_id must be a positive integer")
        
    return True

def process_main_loop(data_stream):
    """Main loop with integrated input validation."""
    for item in data_stream:
        try:
            if validate_input_data(item):
                logger.info(f"Processing task {item['task_id']}")
                # Logic to handle valid data goes here
        except (ValueError, KeyError) as e:
            logger.error(f"Validation failed for input: {e}")
            continue

if __name__ == "__main__":
    mock_stream = [{'task_id': 1, 'payload': 'test'}, {'task_id': -1, 'payload': 'fail'}]
    process_main_loop(mock_stream)