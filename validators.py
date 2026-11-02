import re
from typing import Any, Optional

def validate_input_schema(data: Any, schema: dict) -> bool:
    """Validate dictionary against expected types and keys."""
    if not isinstance(data, dict):
        return False
    
    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_string(value: Any) -> Optional[str]:
    """Clean input strings for safe processing."""
    if not isinstance(value, str):
        return None
    # Remove non-alphanumeric characters excluding standard punctuation
    clean = re.sub(r'[^a-zA-Z0-9\s\.,_-]', '', value)
    return clean.strip()

def process_main_loop(payload: Any) -> None:
    """
    Main processing loop entry point with validation logic.
    Schema: expected input keys and types.
    """
    schema = {'id': int, 'data': str}
    
    if not validate_input_schema(payload, schema):
        raise ValueError("Invalid input payload structure")
    
    sanitized_data = sanitize_string(payload['data'])
    if sanitized_data is None:
        raise ValueError("Corrupted data string provided")
    
    # Proceed with logic using sanitized_data
    print(f"Processing record {payload['id']}: {sanitized_data}")