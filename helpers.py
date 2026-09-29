import os
import shutil
from typing import List, Optional

def clean_directory(directory: str, extensions: Optional[List[str]] = None) -> int:
    """Remove files with specific extensions from a directory."""
    count = 0
    if not os.path.exists(directory):
        return count

    for filename in os.listdir(directory):
        if extensions and not filename.endswith(tuple(extensions)):
            continue
        
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                count += 1
        except OSError:
            continue
    return count

def organize_files(source_dir: str, target_map: dict) -> None:
    """Move files to subdirectories based on extension mapping."""
    if not os.path.exists(source_dir):
        return

    for filename in os.listdir(source_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext in target_map:
            dest_dir = os.path.join(source_dir, target_map[ext])
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))

def ensure_safe_path(base_path: str, user_path: str) -> str:
    """Prevent directory traversal attacks by validating absolute paths."""
    base = os.path.abspath(base_path)
    target = os.path.abspath(os.path.join(base, user_path))
    if not target.startswith(base):
        raise ValueError("invalid path access attempt")
    return target