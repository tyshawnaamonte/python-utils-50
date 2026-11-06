import re

def validate_input_data(data: dict) -> bool:
    """Validates dictionary keys and value formats."""
    required_keys = ['id', 'payload', 'timestamp']
    
    # Ensure all required keys exist
    if not all(k in data for k in required_keys):
        return False
        
    # Validate ID format (must be alphanumeric)
    if not isinstance(data['id'], str) or not data['id'].isalnum():
        return False
        
    # Validate payload is non-empty dictionary
    if not isinstance(data['payload'], dict) or not data['payload']:
        return False
        
    return True

def sanitize_string(value: str) -> str:
    """Removes non-alphanumeric characters from input strings."""
    return re.sub(r'[^a-zA-Z0-9]', '', value)

def process_stream(data_stream: list):
    """Main loop with integrated input validation."""
    processed = []
    for item in data_stream:
        if validate_input_data(item):
            # Clean payload before processing
            item['id'] = sanitize_string(item['id'])
            processed.append(item)
        else:
            continue
    return processed