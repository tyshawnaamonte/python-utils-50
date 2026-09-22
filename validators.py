import re
from typing import Any

def is_email(value: str) -> bool:
    """Validate if the provided string is a standard email format."""
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_pattern, value))

def is_not_empty(value: Any) -> bool:
    """Check if the input is not None and not an empty collection."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set, tuple)):
        return len(value) > 0
    return True

def is_in_range(value: int, min_val: int, max_val: int) -> bool:
    """Verify if a number falls within the inclusive specified range."""
    return isinstance(value, int) and min_val <= value <= max_val

def is_alphanumeric(value: str) -> bool:
    """Verify if the string contains only alphanumeric characters."""
    return value.isalnum()

def validate_schema(data: dict, required_keys: list) -> bool:
    """Confirm that all required keys are present in the dictionary."""
    return all(key in data for key in required_keys)