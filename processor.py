import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensure data is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError(f"Expected dict, got {type(data).__name__}")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return True

def process_payloads(payload_list):
    """Main processing loop with input validation."""
    for index, payload in enumerate(payload_list):
        try:
            validate_input(payload)
            # Perform business logic here
            logger.info(f"Processing payload at index {index}: {payload.get('id', 'unknown')}")
        except ValueError as e:
            logger.error(f"Skipping invalid payload at index {index}: {e}")
        except Exception as e:
            logger.critical(f"Unexpected failure at index {index}: {e}")

if __name__ == "__main__":
    sample_data = [{'id': 1}, {}, 'invalid_string', {'id': 2}]
    process_payloads(sample_data)