import re
from typing import Any

def is_email(email: str) -> bool:
    """Validate standard email format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a non-empty, stripped string."""
    return isinstance(value, str) and bool(value.strip())

def is_port(value: Any) -> bool:
    """Validate network port range (1-65535)."""
    try:
        port = int(value)
        return 1 <= port <= 65535
    except (ValueError, TypeError):
        return False

def validate_dict_keys(data: dict, required_keys: list) -> bool:
    """Verify all keys exist in the provided dictionary."""
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def is_alphanumeric(value: str) -> bool:
    """Check if string contains only alphanumeric characters."""
    return value.isalnum()