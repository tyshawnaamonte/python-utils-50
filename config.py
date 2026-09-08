import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """A utility class to load JSON configurations with default fallbacks."""

    def __init__(
        self, defaults: Dict[str, Any], config_path: Optional[str] = None
    ):
        self.defaults = defaults
        self.config_path = config_path
        self.config = self._load_and_merge()

    def _load_and_merge(self) -> Dict[str, Any]:
        """Loads config from path and merges it with default values."""
        merged = self.defaults.copy()
        if not self.config_path or not os.path.exists(self.config_path):
            return merged

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self._deep_update(merged, user_config)
        except (json.JSONDecodeError, OSError):
            # Fallback to defaults on read error or invalid json
            pass
        return merged

    def _deep_update(
        self, base: Dict[str, Any], updates: Dict[str, Any]
    ) -> None:
        """Recursively updates a dictionary with another dictionary's values."""
        for key, value in updates.items():
            if (
                isinstance(value, dict)
                and key in base
                and isinstance(base[key], dict)
            ):
                self._deep_update(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by dot-notated key or flat key."""
        if "." in key:
            parts = key.split(".")
            current = self.config
            for part in parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    return default
            return current
        return self.config.get(key, default)
