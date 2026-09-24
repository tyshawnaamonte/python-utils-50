import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures required fields exist and types are correct."""
    required = {"id": int, "payload": str}
    for field, expected_type in required.items():
        if field not in data or not isinstance(data[field], expected_type):
            return False
    return True

def run_processing_loop(data_stream: list):
    """Main loop processing valid items from stream."""
    for entry in data_stream:
        # Validate structure before processing
        if not validate_input(entry):
            logger.error(f"Invalid data structure encountered: {entry}")
            continue

        try:
            # Process valid business logic
            process_item(entry)
        except Exception as e:
            logger.exception(f"Runtime error during processing: {e}")

def process_item(item: dict):
    """Placeholder for core business logic."""
    print(f"Processing item {item['id']}: {item['payload']}")

if __name__ == "__main__":
    sample_data = [
        {"id": 1, "payload": "data_one"},
        {"id": "invalid", "payload": "fail"},
        {"id": 2, "payload": "data_two"}
    ]
    run_processing_loop(sample_data)