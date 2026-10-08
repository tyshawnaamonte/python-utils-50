import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from a JSON file with fallback defaults."""
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

class ConfigLoader:
    """Simple helper for managing application settings."""
    def __init__(self, filepath: str, defaults: Dict[str, Any]):
        self.filepath = filepath
        self.defaults = defaults
        self.settings = self.refresh()

    def refresh(self) -> Dict[str, Any]:
        """Reload configuration from disk."""
        self.settings = load_config(self.filepath, self.defaults)
        return self.settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a specific setting value."""
        return self.settings.get(key, default)