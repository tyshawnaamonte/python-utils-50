class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input(data):
    """
    Validates core input types and structures for the processing loop.
    Ensures data is a dictionary with required keys and non-empty values.
    """
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")

    required_keys = {'id', 'payload'}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - data.keys()
        raise ValidationError(f"Missing required keys: {missing}")

    if not data.get('id') or not isinstance(data['payload'], (str, list)):
        raise ValidationError("Invalid payload format or empty identifier")

    return True

def process_with_validation(stream):
    """
    Main loop handler integrating strict validation before processing items.
    """
    for item in stream:
        try:
            if validate_input(item):
                # Simulate logic once validated
                print(f"Processing item {item['id']}")
        except ValidationError as e:
            print(f"Skipping invalid entry: {e}")
            continue