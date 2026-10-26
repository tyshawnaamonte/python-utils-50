import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Utility class for loading application configuration with default values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merge a dictionary of configuration settings into existing config."""
        self._config.update(data)

    def load_from_json(self, filepath: str) -> bool:
        """Load configuration settings from a JSON file if present."""
        if not os.path.isfile(filepath):
            return False
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._config.update(data)
                return True
        return False

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load environment variables matching a prefix into configuration."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option with an optional default fallback."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the combined configuration dictionary."""
        return self._config.copy()

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __contains__(self, key: str) -> bool:
        return key in self._config
