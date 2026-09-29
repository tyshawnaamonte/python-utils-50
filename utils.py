from typing import List, Any, Optional, Dict
import datetime

def format_timestamp(timestamp: float) -> str:
    """Converts a float timestamp into a human-readable ISO string."""
    return datetime.datetime.fromtimestamp(timestamp).isoformat()

def get_nested_value(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """Retrieves a value from a nested dictionary using a list of keys."""
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current

def clean_list(items: List[Optional[str]]) -> List[str]:
    """Removes None values and strips whitespace from a list of strings."""
    return [item.strip() for item in items if item is not None]

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i:i + size] for i in range(0, len(data), size)]