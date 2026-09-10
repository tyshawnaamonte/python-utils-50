import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_CONFIG = {
    "app_name": "App",
    "debug": False,
    "port": 8080,
    "host": "127.0.0.1",
    "log_level": "INFO",
}


def _deep_update(source: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively update target dictionary with override values."""
    result = source.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = _deep_update(result[key], value)
        else:
            result[key] = value
    return result


class ConfigLoader:
    """Utility to manage settings with environment and file overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = (defaults or DEFAULT_CONFIG).copy()

    def load_from_json(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Merge settings from a JSON file into the configuration."""
        path = Path(filepath)
        if path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                self._config = _deep_update(self._config, file_data)
        return self._config

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Parse environment variables matching a prefix into settings."""
        env_data: Dict[str, Any] = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                if value.lower() in ("true", "false"):
                    env_data[config_key] = value.lower() == "true"
                elif value.isdigit():
                    env_data[config_key] = int(value)
                else:
                    env_data[config_key] = value

        self._config = _deep_update(self._config, env_data)
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._config.get(key, default)

    @property
    def values(self) -> Dict[str, Any]:
        """Return the full current configuration dictionary."""
        return self._config.copy()
