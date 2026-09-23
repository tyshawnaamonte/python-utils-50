import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_json(self, filepath: str) -> None:
        """Updates internal config with values from a JSON file."""
        if not os.path.exists(filepath):
            return
        
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self._merge(self.config, user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def _merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Recursively update nested configuration dictionaries."""
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._merge(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self.config.get(key, default)

# Example usage:
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
    loader = ConfigLoader(defaults)
    loader.load_from_json('settings.json')
    print(f"Active host: {loader.get('host')}")