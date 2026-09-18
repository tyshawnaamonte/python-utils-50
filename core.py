from typing import Any, Dict, List, Optional, Union

def merge_configurations(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries for configuration management."""
    merged = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = merge_configurations(merged[key], value)
        else:
            merged[key] = value
    return merged

def format_data_list(items: List[Any], prefix: str = "Item") -> List[str]:
    """Convert list items into a formatted string list with prefixing."""
    return [f"{prefix} {i}: {str(item)}" for i, item in enumerate(items, 1)]

def get_nested_value(data: Dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    """Retrieve nested dictionary values via dot-notation path."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

if __name__ == "__main__":
    config = {"app": {"debug": True, "port": 8080}}
    updates = {"app": {"port": 9000}}
    print(merge_configurations(config, updates))