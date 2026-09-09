from typing import Any, Optional, Dict, List

def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> List[str]:
    """Validate dictionary values against a type schema."""
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"missing required key: {key}")
        elif not isinstance(data[key], expected_type):
            actual = type(data[key]).__name__
            expected = expected_type.__name__
            errors.append(f"key {key} expects {expected}, got {actual}")
    return errors

def sanitize_input(value: Any, default: Any = None) -> Any:
    """Return value if truthy, otherwise default."""
    return value if value else default

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a valid non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0

def extract_field(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Extract value from nested dict using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current if current is not None else default
    except (KeyError, TypeError, AttributeError):
        return default