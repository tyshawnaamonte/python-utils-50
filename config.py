import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading configuration with fallback defaults."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, file_path: str) -> Dict[str, Any]:
        """Load JSON config or return defaults if missing."""
        if not os.path.exists(file_path):
            return self.defaults.copy()

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults.copy()

    def update_defaults(self, new_defaults: Dict[str, Any]) -> None:
        """Overwrite existing default values."""
        self.defaults.update(new_defaults)

def get_app_config(path: str = 'config.json') -> Dict[str, Any]:
    """Helper for quick configuration access."""
    default_settings = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    loader = ConfigLoader(default_settings)
    return loader.load(path)