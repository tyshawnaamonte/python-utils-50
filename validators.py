import re

def validate_input_data(data: dict) -> bool:
    """Validates dictionary structure and contents for processing."""
    required_keys = ['id', 'payload', 'timestamp']
    
    if not isinstance(data, dict):
        return False

    # Check required fields
    if not all(key in data for key in required_keys):
        return False

    # Validate ID format (alphanumeric)
    if not re.match(r'^[a-zA-Z0-9]+$', str(data['id'])):
        return False

    # Validate payload type
    if not isinstance(data['payload'], (str, dict, list)):
        return False

    return True

def sanitize_input(value: str) -> str:
    """Basic sanitization for string inputs."""
    if not isinstance(value, str):
        return str(value)
    return value.strip()[:256]

# Main processing loop utility
def process_stream(data_stream: list):
    """Filter and process validated input items."""
    valid_items = []
    for entry in data_stream:
        if validate_input_data(entry):
            entry['payload'] = sanitize_input(entry['payload'])
            valid_items.append(entry)
    return valid_items