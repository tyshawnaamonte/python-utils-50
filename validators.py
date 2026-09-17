import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input(data: Any, expected_type: type) -> Optional[Any]:
    """Ensures input matches expected type with edge case handling."""
    try:
        if data is None:
            raise ValueError("input data cannot be null")
        
        if not isinstance(data, expected_type):
            raise TypeError(f"expected {expected_type.__name__}, got {type(data).__name__}")
            
        return data
    except (ValueError, TypeError) as e:
        logger.error(f"validation failure: {e}")
        return None

def safe_int_conversion(value: Any, default: int = 0) -> int:
    """Converts values to int with fallback for errors."""
    try:
        if isinstance(value, (int, float)):
            return int(value)
        if isinstance(value, str):
            return int(value.strip())
        raise ValueError("unsupported type for conversion")
    except (ValueError, TypeError, AttributeError) as e:
        logger.warning(f"conversion failed for {value}: {e}. returning default.")
        return default

def validate_non_empty_string(value: Any) -> str:
    """Checks if string is not empty or whitespace only."""
    if not isinstance(value, str):
        return ""
    stripped = value.strip()
    return stripped if stripped else ""