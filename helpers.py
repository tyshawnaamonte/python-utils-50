from typing import Any, Dict, Generator, Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def chunk_iterable(
    iterable: Iterable[T], size: int
) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from an iterable.

    Args:
        iterable: The collection or iterator to slice into chunks.
        size: Maximum number of elements per chunk. Must be greater than zero.

    Yields:
        Lists containing up to `size` elements from the original iterable.
    """
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary by concatenating keys with a separator.

    Args:
        d: The nested dictionary to flatten.
        parent_key: Prefix for flattened keys, used during recursion.
        sep: String separator used between nested keys.

    Returns:
        A single-level dictionary with compound keys.
    """
    items: List[Tuple[str, Any]] = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def format_bytes(size_in_bytes: int) -> str:
    """Convert a byte count into a human-readable string representation.

    Args:
        size_in_bytes: Non-negative integer representing size in bytes.

    Returns:
        Formatted string representation with units (e.g., '1.50 MB').
    """
    if size_in_bytes < 0:
        raise ValueError("Byte size cannot be negative.")

    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(size_in_bytes)
    unit_index = 0

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"
