import collections.abc
from typing import Any, Dict, List, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Uses dot notation for nested keys.
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none_values(data: Any) -> Any:
    """
    Recursively removes None values from dicts and lists.
    """
    if isinstance(data, dict):
        return {k: filter_none_values(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [filter_none_values(i) for i in data if i is not None]
    return data

def get_nested_value(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Retrieves a value from a nested dict using a dot-separated path.
    """
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default