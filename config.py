"""Configuration management utilities for general Python applications."""

import os
from typing import Any, Dict, Optional, Union


class ConfigManager:
    """Manages application configuration settings with environment variable fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the ConfigManager with optional default settings."""
        self._settings: Dict[str, Any] = defaults.copy() if defaults else {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key, checking environment variables first."""
        env_key = key.upper()
        if env_key in os.environ:
            return self._parse_env_value(os.environ[env_key])
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value programmatically."""
        self._settings[key] = value

    def load_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """Bulk load configuration settings from a dictionary."""
        self._settings.update(config_dict)

    @staticmethod
    def _parse_env_value(val: str) -> Union[int, float, bool, str]:
        """Parse string values from environment variables into appropriate types."""
        if val.lower() in ("true", "yes", "1"):
            return True
        if val.lower() in ("false", "no", "0"):
            return False
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            pass
        return val
