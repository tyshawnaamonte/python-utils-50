import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading of configuration files with default overrides."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads json configuration merging it with default values."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}")
            
        return config

    def load_from_env(self, prefix: str) -> Dict[str, Any]:
        """Extracts configuration settings from environment variables."""
        env_config = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                env_config[config_key] = value
        return env_config