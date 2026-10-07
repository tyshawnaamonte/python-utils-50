from typing import List, Any, Optional, Dict
import json

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a multi-dimensional list into a single list."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def safe_json_load(data: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parse json string safely with a default return value."""
    try:
        return json.loads(data)
    except (ValueError, TypeError):
        return default or {}

def chunk_iterable(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + size] for i in range(0, len(items), size)]

def get_nested_key(data: Dict[str, Any], keys: List[str]) -> Any:
    """Access deeply nested dictionaries via a list of keys."""
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current