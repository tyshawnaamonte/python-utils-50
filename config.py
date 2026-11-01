import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility for loading application configuration with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults: Dict[str, Any] = defaults or {}

    def load_from_dict(self, config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Merge provided dictionary with default configurations."""
        merged = self.defaults.copy()
        merged.update(config_dict)
        return merged

    def load_from_json(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file, falling back to defaults."""
        path = Path(filepath)
        if not path.is_file():
            return self.defaults.copy()

        with open(path, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

        if isinstance(loaded_data, dict):
            return self.load_from_dict(loaded_data)
        return self.defaults.copy()

    def load_from_env(self, prefix: str = "") -> Dict[str, Any]:
        """Extract configuration overrides from environment variables."""
        result = self.defaults.copy()
        for key, default_val in self.defaults.items():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                if isinstance(default_val, bool):
                    result[key] = raw_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    result[key] = int(raw_val)
                elif isinstance(default_val, float):
                    result[key] = float(raw_val)
                else:
                    result[key] = raw_val
        return result


def load_config(
    filepath: Optional[Union[str, Path]] = None,
    defaults: Optional[Dict[str, Any]] = None,
    env_prefix: str = "",
) -> Dict[str, Any]:
    """Convenience function to load config from file and environment."""
    loader = ConfigLoader(defaults=defaults)
    config = loader.defaults.copy()

    if filepath:
        config = loader.load_from_json(filepath)

    if defaults:
        env_loader = ConfigLoader(defaults=config)
        config = env_loader.load_from_env(prefix=env_prefix)

    return config
