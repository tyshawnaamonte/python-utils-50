from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Utility class for processing dictionary data with validation."""

    def __init__(self, fallback_value: Any = None) -> None:
        """Initialize the handler with an optional fallback value."""
        self.fallback = fallback_value

    def get_nested(self, data: Dict[str, Any], path: str) -> Any:
        """Retrieve value from nested dictionary using dot notation."""
        keys = path.split('.')
        current = data

        try:
            for key in keys:
                current = current[key]
            return current
        except (KeyError, TypeError):
            return self.fallback

    def apply_transform(self, data: Dict[str, Any], func: Callable[[Any], Any], key: str) -> Dict[str, Any]:
        """Apply transformation function to a specific key."""
        if key in data:
            data[key] = func(data[key])
        return data

    def validate_keys(self, data: Dict[str, Any], required: list[str]) -> bool:
        """Check if all required keys exist in dictionary."""
        return all(key in data for key in required)