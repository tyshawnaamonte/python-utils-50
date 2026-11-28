from typing import Any, Iterable, Dict, List, Optional

def flatten_list(items: Iterable[Any]) -> List[Any]:
    """Recursively flatten a nested list structure into a single list."""
    result: List[Any] = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_iterable(data: Iterable[Any], size: int) -> Iterable[List[Any]]:
    """Split an iterable into smaller chunks of a specified size."""
    chunk: List[Any] = []
    for item in data:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any], overwrite: bool = True) -> Dict[Any, Any]:
    """Merge two dictionaries, optionally allowing overwrites for shared keys."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key not in result or overwrite:
            result[key] = value
    return result

def get_nested(data: Dict[Any, Any], keys: List[Any], default: Optional[Any] = None) -> Any:
    """Retrieve a value from a nested dictionary using a list of keys."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, IndexError):
        return default