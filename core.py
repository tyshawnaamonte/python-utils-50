import json
import logging
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-50')

def safe_json_load(file_path: str) -> Optional[Dict[str, Any]]:
    """Load json file safely with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"failed to load {file_path}: {e}")
        return None

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split list into smaller chunks of specific size."""
    if size <= 0:
        raise ValueError("chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_nested(data: Dict[str, Any], path: List[str], default: Any = None) -> Any:
    """Access nested dictionary keys safely."""
    current = data
    for key in path:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
    return current if current is not None else default