import functools
import time
from typing import Any, Callable, Generator, Iterable, List, TypeVar

T = TypeVar("T")


def memoize_with_ttl(ttl_seconds: float = 60.0) -> Callable:
    """Decorator that caches function results with a time-to-live expiration."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        cache: dict[tuple, tuple[Any, float]] = {}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result

        return wrapper

    return decorator


def batch_stream(
    iterable: Iterable[T], batch_size: int = 100
) -> Generator[List[T], None, None]:
    """Efficiently yield items from iterable in fixed-size batches to reduce memory footprint."""
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")

    batch: List[T] = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
