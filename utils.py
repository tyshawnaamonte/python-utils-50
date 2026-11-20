import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes dictionary data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (IOError, TypeError):
        return False

def get_nested_key(data: Dict[str, Any], keys: list, default: Any = None) -> Any:
    """Retrieves a nested dictionary value using a key list."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def sanitize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}