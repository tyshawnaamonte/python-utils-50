import json
import os
from typing import Any, Dict, Optional

def load_json_file(path: str) -> Dict[str, Any]:
    """Safe loading of JSON configuration files."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(path: str, data: Dict[str, Any]) -> bool:
    """Atomic-like saving of dictionary to JSON."""
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Fetch environment variable with fallback default."""
    return os.environ.get(key, default)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary for flat config structures."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)