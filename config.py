import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration and merges with provided defaults."""
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration dictionary to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# Example usage implementation
if __name__ == "__main__":
    default_settings = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    current_cfg = load_config("config.json", default_settings)
    print(f"Loaded config: {current_cfg}")