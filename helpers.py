import json
from typing import Any, Dict, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested values from dictionaries using dot notation."""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively remove None values from a dictionary."""
    return {
        k: clean_dict(v) if isinstance(v, dict) else v
        for k, v in data.items()
        if v is not None
    }

def to_json_str(data: Any, indent: int = 2) -> str:
    """Serialize data to formatted JSON string."""
    return json.dumps(data, indent=indent, default=str)

def safe_parse_json(raw_data: str) -> Optional[Dict[str, Any]]:
    """Safely parse JSON strings with error catching."""
    try:
        return json.loads(raw_data)
    except (ValueError, TypeError):
        return None