from typing import Any, Dict, List, Optional

def sanitize_data(data: Any, key_filter: Optional[List[str]] = None) -> Any:
    """
    Recursively cleans dictionaries, removing filtered keys and handling nulls.
    """
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if key_filter and key in key_filter:
                continue
            if value is not None:
                result[key] = sanitize_data(value, key_filter)
        return result
    
    if isinstance(data, list):
        return [sanitize_data(item, key_filter) for item in data]
    
    return data

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens nested dictionary structures into a single-level dictionary.
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)