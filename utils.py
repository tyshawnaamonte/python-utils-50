import os
from typing import Any, List, Optional, Union

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Perform division with error handling for zero and invalid types."""
    if a is None or b is None:
        return None
    try:
        return float(a) / float(b)
    except (TypeError, ValueError, ZeroDivisionError):
        return None

def safe_file_read(path: str) -> Optional[str]:
    """Read file contents handling missing files and permissions."""
    if not path or not isinstance(path, str):
        return None
    try:
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except (OSError, IOError, PermissionError):
        return None

def calculate_average(data: List[Union[int, float]]) -> float:
    """Compute average handling empty lists and non-numeric data."""
    if not data or not isinstance(data, (list, tuple)):
        return 0.0
    try:
        valid_numbers = [x for x in data if isinstance(x, (int, float))]
        if not valid_numbers:
            return 0.0
        return sum(valid_numbers) / len(valid_numbers)
    except (TypeError, ValueError):
        return 0.0

def parse_to_int(value: Any, default: int = 0) -> int:
    """Convert value to int with fallback for errors."""
    if value is None:
        return default
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default

def safe_get_dict_value(data: dict, key: str, default: Any = None) -> Any:
    """Safely retrieve value from dict handling missing keys."""
    if not isinstance(data, dict):
        return default
    try:
        return data.get(key, default)
    except (AttributeError, TypeError):
        return default