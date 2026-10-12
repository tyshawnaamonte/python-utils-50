import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigManager:
    """Manages application configuration loading and key-value access."""

    def __init__(self, config_path: Optional[Union[str, Path]] = None) -> None:
        """Initialize ConfigManager with an optional file path."""
        self.config_path: Optional[Path] = Path(config_path) if config_path else None
        self._data: Dict[str, Any] = {}
        if self.config_path and self.config_path.exists():
            self.load()

    def load(self) -> None:
        """Load configuration settings from a JSON file."""
        if not self.config_path:
            raise ValueError("No configuration path specified.")

        with open(self.config_path, "r", encoding="utf-8") as file:
            self._data = json.load(file)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key or environment fallback."""
        if key in self._data:
            return self._data[key]
        return os.environ.get(key.upper(), default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration key-value pair in memory."""
        self._data[key] = value

    def save(self, target_path: Optional[Union[str, Path]] = None) -> None:
        """Save current memory configuration to a JSON file."""
        path = Path(target_path) if target_path else self.config_path
        if not path:
            raise ValueError("Destination path not provided for saving configuration.")

        with open(path, "w", encoding="utf-8") as file:
            json.dump(self._data, file, indent=4)

    def as_dict(self) -> Dict[str, Any]:
        """Return a copy of the configuration dictionary."""
        return self._data.copy()
