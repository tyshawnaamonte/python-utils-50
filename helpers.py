import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns the merged dictionary.
    """
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(path: str, config: Dict[str, Any]) -> None:
    """
    Persists configuration dictionary to a JSON file.
    """
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)
