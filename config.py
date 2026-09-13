import os
import json
from typing import Any, Dict, Optional


class ConfigManager:
    """Simple configuration manager loading from dict or environment variables."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value, checking environment variables first."""
        env_val = os.getenv(key.upper())
        if env_val is not None:
            return env_val
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value in memory."""
        self._config[key] = value

    def load_from_json(self, filepath: str) -> None:
        """Load configuration key-value pairs from a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._config.update(data)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration dictionary."""
        return self._config.copy()
