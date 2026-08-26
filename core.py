import json
import os
from typing import Any, Dict, List, Optional


def load_json_file(filepath: str) -> Optional[Dict[str, Any]]:
    """Load and parse a JSON file safely, returning None on failure."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def save_json_file(filepath: str, data: Any) -> bool:
    """Save data to a JSON file with indentation."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except (TypeError, IOError):
        return False


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary using a separator."""
    items: List[tuple] = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
