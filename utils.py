from typing import Dict, Any


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single-level dictionary.

    Args:
        d: The nested dictionary to flatten.
        parent_key: The accumulated parent key string.
        sep: Separator used between nested keys.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten_dict(d: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    """Unflattens a single-level dictionary with separated keys back into nested form.

    Args:
        d: The flattened dictionary.
        sep: Separator used to split keys.
    """
    result: Dict[str, Any] = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result
