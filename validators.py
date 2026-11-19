import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validates standard email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_range(value: Any, min_val: float, max_val: float) -> bool:
    """Checks if a numeric value falls within inclusive range."""
    if not isinstance(value, (int, float)):
        return False
    return min_val <= value <= max_val

def is_non_empty_string(value: Any) -> bool:
    """Ensures input is a string and contains non-whitespace content."""
    return isinstance(value, str) and bool(value.strip())

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Returns value if valid string, otherwise returns default."""
    return value if is_non_empty_string(value) else default

def validate_schema(data: dict, keys: list) -> bool:
    """Verifies all required keys exist in dictionary."""
    return all(key in data for key in keys)