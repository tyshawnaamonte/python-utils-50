from typing import Any, Dict, List, Optional

def deep_flatten(items: List[Any]) -> List[Any]:
    """Recursively flattens a nested list structure."""
    flat = []
    for item in items:
        if isinstance(item, list):
            flat.extend(deep_flatten(item))
        else:
            flat.append(item)
    return flat

def merge_dicts(base: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries recursively."""
    result = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def sanitize_keys(data: Dict[str, Any], forbidden: List[str]) -> Dict[str, Any]:
    """Removes sensitive keys from a dictionary."""
    return {k: v for k, v in data.items() if k not in forbidden}

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Divides list into smaller chunks of specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i:i + size] for i in range(0, len(items), size)]