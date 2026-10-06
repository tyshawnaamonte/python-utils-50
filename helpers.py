import os
import logging
from typing import Any, List, Optional

logger = logging.getLogger(__name__)

def sanitize_path(path: str) -> str:
    """Normalize and clean system file paths."""
    return os.path.normpath(path.strip())

def get_environment_variable(key: str, default: Optional[str] = None) -> str:
    """Fetch environment variable with safe fallback."""
    return os.environ.get(key, default or "")

def batch_process(items: List[Any], chunk_size: int = 10) -> List[List[Any]]:
    """Split list into smaller executable chunks."""
    if chunk_size <= 0:
        return [items]
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def validate_directory(path: str) -> bool:
    """Check if path exists and is a directory."""
    try:
        full_path = sanitize_path(path)
        return os.path.isdir(full_path)
    except Exception as e:
        logger.error(f"validation failed for {path}: {e}")
        return False

def cleanup_temp_files(directory: str, extension: str = ".tmp") -> int:
    """Remove temporary files from specified directory."""
    count = 0
    if not validate_directory(directory):
        return count

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            count += 1
    return count