import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self._defaults = default_config

    def load(self, file_path: str) -> Dict[str, Any]:
        """Loads config from file or returns defaults if missing."""
        config = self._defaults.copy()

        if not os.path.exists(file_path):
            return config

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

def get_app_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function for configuration initialization."""
    loader = ConfigLoader(defaults)
    return loader.load(file_path)