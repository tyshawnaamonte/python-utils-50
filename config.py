import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility for loading configuration settings with default fallback values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}

    def load_dict(self, config_data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge custom configuration dictionary over default settings."""
        merged = self.defaults.copy()
        merged.update(config_data)
        return merged

    def load_json(
        self, filepath: Union[str, Path], env_prefix: Optional[str] = None
    ) -> Dict[str, Any]:
        """Load config from a JSON file with optional environment variable overrides."""
        config = self.defaults.copy()
        path = Path(filepath)

        if path.exists() and path.is_file():
            with open(path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    config.update(file_config)

        if env_prefix:
            prefix = f"{env_prefix.upper()}_"
            for env_key, env_val in os.environ.items():
                if env_key.startswith(prefix):
                    setting_key = env_key[len(prefix) :].lower()
                    config[setting_key] = self._cast_value(env_val)

        return config

    @staticmethod
    def _cast_value(val: str) -> Any:
        """Attempt basic type casting for string values from environment variables."""
        lowered = val.strip().lower()
        if lowered in ("true", "yes", "1"):
            return True
        if lowered in ("false", "no", "0"):
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
