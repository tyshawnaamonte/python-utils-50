import json
from typing import Any, Dict, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested values using dot notation path."""
    keys = path.split('.')
    val = data
    try:
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError, IndexError):
        return default

def format_json(data: Any, indent: int = 4) -> str:
    """Serialize data to a clean, readable JSON string."""
    return json.dumps(data, indent=indent, sort_keys=True)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_input(data: Any) -> Any:
    """Basic sanitization for string inputs to prevent injection."""
    if isinstance(data, str):
        return data.strip().replace('<', '&lt;').replace('>', '&gt;')
    if isinstance(data, dict):
        return {k: sanitize_input(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_input(v) for v in data]
    return data