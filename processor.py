from typing import Iterable, Generator, Any, Type, TypeVar, List

T = TypeVar('T')

def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of size chunk_size from the given iterable."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def safe_cast(value: Any, to_type: Type[T], default: T) -> T:
    """Safely cast a value to a given type, returning the default if casting fails."""
    try:
        if value is None:
            return default
        return to_type(value)
    except (ValueError, TypeError):
        return default


def deep_flatten(nested_iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """Flatten a nested iterable of arbitrary depth, ignoring strings as iterables."""
    for item in nested_iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item
