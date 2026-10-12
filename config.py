import os
from typing import Any, Dict

class Config:
    """Centralized configuration management for project utilities."""
    
    def __init__(self, env_prefix: str = "UTILS_"):
        self.env_prefix = env_prefix
        self._settings: Dict[str, Any] = {}
        self._load_from_env()

    def _load_from_env(self) -> None:
        """Loads environment variables with the specified prefix."""
        for key, value in os.environ.items():
            if key.startswith(self.env_prefix):
                clean_key = key[len(self.env_prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key."""
        return self._settings.get(key.lower(), default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update settings with a provided dictionary."""
        for key, value in new_settings.items():
            self._settings[key.lower()] = value

def get_default_config() -> Config:
    """Factory function for standard utility configuration."""
    return Config()