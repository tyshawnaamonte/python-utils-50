import math
from typing import Any, Dict, Generator, Sequence, Optional


def format_bytes(size_bytes: int) -> str:
    """Convert a byte count into a human-readable string representation."""
    if size_bytes < 0:
        raise ValueError("Size cannot be negative.")
    if size_bytes == 0:
        return "0 B"
    units = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {units[i]}"


def chunkify(items: Sequence[Any], chunk_size: int) -> Generator[Sequence[Any], None, None]:
    """Yield successive fixed-size chunks from a given sequence."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]


def get_nested(data: Dict[str, Any], path: str, default: Optional[Any] = None, delimiter: str = ".") -> Any:
    """Safely retrieve a nested dictionary value using a delimited path string."""
    keys = path.split(delimiter)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, adding a suffix if shortened."""
    if len(text) <= max_length:
        return text
    if max_length < len(suffix):
        return text[:max_length]
    return text[: max_length - len(suffix)] + suffix
