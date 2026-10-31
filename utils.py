"""General utility functions for data manipulation and safe type conversion."""

import collections.abc
from typing import Any, Dict, Generator, Iterable, List, Optional, Type, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from an iterable.

    Args:
        iterable: The sequence or iterable to split into chunks.
        chunk_size: Maximum number of elements in each chunk.

    Yields:
        Lists containing up to `chunk_size` elements.

    Raises:
        ValueError: If chunk_size is less than 1.
    """
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")

    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def flatten_dict(
    nested_dict: Dict[str, Any],
    parent_key: str = "",
    sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary by concatenating keys with a separator.

    Args:
        nested_dict: The dictionary containing nested dictionary values.
        parent_key: Prefix for keys at the current recursion level.
        sep: String separator used between nested keys.

    Returns:
        A single-level dictionary with flattened key paths.
    """
    items: List[tuple] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, collections.abc.Mapping):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def safe_cast(val: Any, to_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    """Safely convert a value to a target type with fallback.

    Args:
        val: The value to be cast.
        to_type: The target class or type function.
        default: Fallback value returned if conversion fails.

    Returns:
        The converted value, or default if casting raises ValueError or TypeError.
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
