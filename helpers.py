import os
import json
import time
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    """Reads and parses a json file into a dictionary."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """Serializes data to a json file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def retry_operation(func, retries: int = 3, delay: float = 1.0):
    """Retries a function call upon failure."""
    last_ex = None
    for _ in range(retries):
        try:
            return func()
        except Exception as e:
            last_ex = e
            time.sleep(delay)
    raise last_ex

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens nested dictionary structures."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)