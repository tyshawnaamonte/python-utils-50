import os
import json
from typing import Any, Optional

def load_json(filepath: str) -> dict:
    """Read and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: dict) -> None:
    """Write dictionary data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env(key: str, default: Optional[str] = None) -> Any:
    """Retrieve environment variable with default fallback."""
    return os.environ.get(key, default)

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Normalize path and ensure absolute format."""
    return os.path.abspath(os.path.expanduser(path))