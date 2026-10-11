from typing import Any, Iterable, Optional, TypeVar, List

T = TypeVar('T')

def flatten(items: Iterable[Any]) -> List[Any]:
    """Recursively flatten a nested list structure into a single list."""
    result: List[Any] = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def chunk_list(data: List[T], size: int) -> Iterable[List[T]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    for i in range(0, len(data), size):
        yield data[i:i + size]

def get_nested(data: dict, keys: List[str], default: Any = None) -> Any:
    """Retrieve a value from a nested dictionary using a path of keys."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def ensure_list(value: Any) -> List[Any]:
    """Wrap a single value into a list or return the original list."""
    if value is None:
        return []
    return value if isinstance(value, (list, tuple)) else [value]