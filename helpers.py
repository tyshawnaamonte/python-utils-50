import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict) -> bool:
    """Validates dictionary structure for processing."""
    required_keys = {'id', 'payload', 'timestamp'}
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def process_main_loop(items: list):
    """Main execution loop with input verification."""
    for index, item in enumerate(items):
        try:
            if not validate_input_data(item):
                logger.warning(f"Skipping invalid item at index {index}")
                continue

            # Simulate core logic execution
            result = f"Processed {item['id']}"
            print(result)

        except Exception as e:
            logger.error(f"Unexpected error processing item {index}: {e}")

def clean_and_normalize(raw_data: list) -> list:
    """Sanitize inputs before loop entry."""
    return [i for i in raw_data if isinstance(i, dict)]