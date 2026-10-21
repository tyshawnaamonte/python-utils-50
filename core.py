import functools
from typing import Any, Callable, Dict, List, Tuple


class FastCacheManager:
    """Core caching and execution pipeline optimized for high-throughput data processing."""

    __slots__ = ('_cache', '_maxsize', '_hits', '_misses')

    def __init__(self, maxsize: int = 1024) -> None:
        self._cache: Dict[str, Any] = {}
        self._maxsize: int = maxsize
        self._hits: int = 0
        self._misses: int = 0

    def get_or_compute(self, key: str, compute_fn: Callable[[], Any]) -> Any:
        """Fetch result from cache or compute and store it efficiently."""
        if key in self._cache:
            self._hits += 1
            return self._cache[key]

        self._misses += 1
        result = compute_fn()

        # Fast FIFO eviction if capacity reached
        if len(self._cache) >= self._maxsize:
            first_key = next(iter(self._cache))
            del self._cache[first_key]

        self._cache[key] = result
        return result

    def batch_process(self, items: List[Dict[str, Any]], key_field: str, transform_fn: Callable[[Any], Any]) -> List[Dict[str, Any]]:
        """Optimized batch transformation leveraging internal cache to eliminate duplicate work."""
        cache = self._cache
        maxsize = self._maxsize
        results = []

        for item in items:
            raw_val = item.get(key_field)
            if raw_val is None:
                results.append(item)
                continue

            cache_key = f"{key_field}:{raw_val}"
            if cache_key in cache:
                self._hits += 1
                transformed = cache[cache_key]
            else:
                self._misses += 1
                transformed = transform_fn(raw_val)
                if len(cache) >= maxsize:
                    del cache[next(iter(cache))]
                cache[cache_key] = transformed

            updated_item = item.copy()
            updated_item[key_field] = transformed
            results.append(updated_item)

        return results

    def stats(self) -> Tuple[int, int, float]:
        """Return hit count, miss count, and hit ratio."""
        total = self._hits + self._misses
        ratio = (self._hits / total) if total > 0 else 0.0
        return self._hits, self._misses, round(ratio, 4)
