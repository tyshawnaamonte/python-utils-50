import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with default values."""

    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config

    def load(self, file_path: str) -> Dict[str, Any]:
        """Load config from file and merge with defaults."""
        config = self.defaults.copy()

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    file_data = json.load(f)
                    config.update(file_data)
            except (json.JSONDecodeError, IOError):
                pass

        return config

def get_app_config(path: str, overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Helper to retrieve application settings."""
    loader = ConfigLoader(overrides)
    return loader.load(path)