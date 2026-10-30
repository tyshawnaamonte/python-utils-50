import logging

logger = logging.getLogger(__name__)

def process_payloads(payloads):
    """Iterates through payloads with strict validation checks."""
    for index, data in enumerate(payloads):
        try:
            if not isinstance(data, dict):
                raise ValueError(f"payload at index {index} is not a dictionary")
            
            if 'id' not in data or 'value' not in data:
                raise KeyError(f"missing required keys in payload {index}")
            
            if not isinstance(data['id'], int):
                raise TypeError(f"id field must be an integer at index {index}")

            perform_operation(data)
            
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"validation failure: {e}")
            continue

def perform_operation(data):
    """Internal handler for valid data packets."""
    result = data['value'] * 2
    logger.info(f"processed {data['id']}: result {result}")

if __name__ == "__main__":
    sample_data = [{'id': 1, 'value': 10}, 'invalid', {'id': 2, 'value': 'error'}]
    process_payloads(sample_data)