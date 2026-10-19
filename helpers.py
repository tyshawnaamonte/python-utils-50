"""Helper functions for common Python operations and data structures."""

from typing import Any, Dict, Generator, Iterable, List, Optional, Type, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Split an iterable into chunks of specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    
    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def safe_cast(value: Any, to_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    """Attempt to cast a value to a target type, returning default on failure."""
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length, preserving suffix if truncated."""
    if len(text) <= max_length:
        return text
    if max_length < len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix
