import time
from functools import wraps
from typing import Any, Callable, Dict, Generator, Iterable, List, TypeVar

T = TypeVar("T")


def timed_lru_cache(seconds: int, maxsize: int = 128) -> Callable:
    """Decorator providing an LRU cache with time-based expiration (TTL)."""
    def decorator(func: Callable) -> Callable:
        cache: Dict[tuple, tuple[Any, float]] = {}

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()

            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result

            result = func(*args, **kwargs)
            if len(cache) >= maxsize and key not in cache:
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            cache[key] = (result, now)
            return result

        return wrapper
    return decorator


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Efficiently split an iterable into chunks of specified size using memory-friendly yield."""
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


def fast_flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Iterative, memory-optimized dictionary flattening to reduce call stack overhead."""
    items: Dict[str, Any] = {}
    stack = [(d, parent_key)]

    while stack:
        curr, prefix = stack.pop()
        for k, v in curr.items():
            new_key = f"{prefix}{sep}{k}" if prefix else str(k)
            if isinstance(v, dict) and v:
                stack.append((v, new_key))
            else:
                items[new_key] = v

    return items
