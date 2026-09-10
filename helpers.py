from typing import Any, Iterable, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

def chunk_list(data: Iterable[Any], size: int) -> List[List[Any]]:
    """Split an iterable into smaller chunks of a fixed size."""
    data_list = list(data)
    return [data_list[i:i + size] for i in range(0, len(data_list), size)]

def get_nested(data: Dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    """Access a nested dictionary value using a dot-notation string."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default