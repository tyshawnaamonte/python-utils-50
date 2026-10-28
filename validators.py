from typing import Any, Dict, List, Optional

def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> List[str]:
    """Verify data dictionary against a provided type schema."""
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"missing required key: {key}")
        elif not isinstance(data[key], expected_type):
            errors.append(f"invalid type for {key}: expected {expected_type.__name__}")
    return errors

def sanitize_string(value: Any, default: str = "") -> str:
    """Ensure value is a string, stripping whitespace."""
    if not isinstance(value, str):
        return default
    return value.strip()

def ensure_list(value: Any) -> List[Any]:
    """Normalize input into a list."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def is_non_empty_dict(data: Any) -> bool:
    """Check if variable is a non-empty dictionary."""
    return isinstance(data, dict) and len(data) > 0

def get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """Retrieve value from nested dictionary using dot notation."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current