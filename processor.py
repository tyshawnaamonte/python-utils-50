"""Data processing utilities for handling nested structures and collections."""

from typing import Any, Dict, Generator, List, Sequence, TypeVar

T = TypeVar("T")


def flatten_dict(
    data: Dict[str, Any],
    parent_key: str = "",
    sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary using key concatenation."""
    items: List[tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def unflatten_dict(
    data: Dict[str, Any],
    sep: str = "."
) -> Dict[str, Any]:
    """Reconstruct a nested dictionary from a flattened dictionary."""
    result: Dict[str, Any] = {}
    for key, value in data.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def chunk_iterable(
    iterable: Sequence[T],
    chunk_size: int
) -> Generator[List[T], None, None]:
    """Yield successive fixed-size chunks from a sequence."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(iterable), chunk_size):
        yield list(iterable[i : i + chunk_size])
