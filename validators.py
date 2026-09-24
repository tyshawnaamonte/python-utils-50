import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict, required_keys: list) -> bool:
    """Ensures payload contains necessary keys and values."""
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dict")
        return False

    for key in required_keys:
        if key not in data or data[key] is None:
            logger.warning(f"Missing or null field: {key}")
            return False
            
    return True

def process_main_loop(items: list):
    """Main loop entry point with validation logic."""
    required = ['id', 'payload']
    processed = []

    for item in items:
        if validate_input_data(item, required):
            # Logic for valid item processing
            try:
                item['processed'] = True
                processed.append(item)
            except Exception as e:
                logger.error(f"Unexpected error during processing: {e}")
        else:
            logger.info("Skipping invalid item in loop")
            
    return processed