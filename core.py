"""Core utility functions with robust error handling for common edge cases."""

from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
import logging

logger = logging.getLogger(__name__)

T = TypeVar("T")


def safe_get(data: Any, keys: Union[str, List[Any]], default: Any = None) -> Any:
    """Safely retrieve nested values from dictionaries or lists with bounds checking."""
    if isinstance(keys, str):
        keys = keys.split(".")

    curr = data
    for key in keys:
        if isinstance(curr, dict):
            if key not in curr:
                return default
            curr = curr[key]
        elif isinstance(curr, (list, tuple)):
            try:
                idx = int(key)
                if idx < -len(curr) or idx >= len(curr):
                    return default
                curr = curr[idx]
            except (ValueError, TypeError):
                return default
        else:
            return default
    return curr


def safe_cast(val: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Cast a value to a target type, returning default on ValueError/TypeError."""
    if val is None:
        return default
    try:
        return to_type(val)
    except (ValueError, TypeError, OverflowError) as err:
        logger.debug("Failed to cast %r to %s: %s", val, to_type.__name__, err)
        return default


def safe_divide(
    numerator: Union[int, float],
    denominator: Union[int, float],
    default: float = 0.0,
) -> float:
    """Perform division safely, returning default on ZeroDivisionError or TypeError."""
    try:
        return float(numerator) / float(denominator)
    except (ZeroDivisionError, TypeError, ValueError):
        return default


def execute_with_fallback(
    func: Callable[..., T],
    *args: Any,
    fallback: Optional[T] = None,
    expected_exceptions: tuple = (Exception,),
    **kwargs: Any,
) -> Optional[T]:
    """Execute a callable and return a fallback value if an expected exception occurs."""
    try:
        return func(*args, **kwargs)
    except expected_exceptions as err:
        logger.warning("Execution failed for %s: %s", getattr(func, '__name__', str(func)), err)
        return fallback
