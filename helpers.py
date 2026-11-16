import re
from typing import Any, Dict, Iterable, List, Generator, Union


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def chunk_iterable(
    iterable: Iterable[Any], size: int
) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def safe_get(
    data: Dict[str, Any], path: Union[str, List[str]], default: Any = None
) -> Any:
    """Safely retrieve nested values from a dictionary using a path."""
    keys = path.split(".") if isinstance(path, str) else path
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def slugify(text: str) -> str:
    """Convert string to a clean, lowercase URL-friendly slug."""
    text = str(text).lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)
