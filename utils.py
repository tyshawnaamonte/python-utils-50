import json
from typing import Any, Dict, List, Optional
import os

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Any, filepath: str) -> None:
    """Serialize data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of fixed size."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def flatten_list(nested: List[List[Any]]) -> List[Any]:
    """Flatten a list of lists into a single list."""
    return [item for sublist in nested for item in sublist]

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with optional default fallback."""
    return os.environ.get(key, default or "")

def ensure_dir(directory: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)