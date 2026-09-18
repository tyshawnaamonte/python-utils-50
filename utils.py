import os
import shutil
from pathlib import Path
from typing import Union, List

def ensure_directory(path: Union[str, Path]) -> Path:
    """Creates directory if not exists and returns Path object."""
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target

def clean_directory(directory: Union[str, Path]) -> None:
    """Removes all contents within the specified directory."""
    path = Path(directory)
    if not path.is_dir():
        return
    for item in path.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def list_files_by_extension(directory: str, extension: str) -> List[Path]:
    """Returns filtered list of files with given extension."""
    return list(Path(directory).glob(f"*.{extension.lstrip('.')}"))

def safe_remove(path: Union[str, Path]) -> bool:
    """Attempts to remove a file, returns success status."""
    try:
        file_path = Path(path)
        if file_path.exists():
            file_path.unlink()
            return True
    except OSError:
        return False
    return False

def format_byte_size(size_bytes: int) -> str:
    """Converts raw bytes into human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"