from typing import Any, Dict, List, Optional, Union

def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def extract_by_keys(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Extract a subset of keys from a dictionary."""
    return {k: data[k] for k in keys if k in data}

def format_byte_size(size_bytes: int) -> str:
    """Convert bytes to human-readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def ensure_list(item: Union[Any, List[Any]]) -> List[Any]:
    """Force input into a list if not already one."""
    if isinstance(item, list):
        return item
    return [item] if item is not None else []