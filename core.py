import time
from functools import wraps
from threading import RLock
from typing import Callable, Any, Dict, Tuple

class TTLCache:
    """
    A thread-safe in-memory cache with Time-To-Live (TTL) expiration.
    """
    def __init__(self, default_ttl: float = 300.0):
        self.default_ttl = default_ttl
        self._cache: Dict[Any, Tuple[Any, float]] = {}
        self._lock = RLock()

    def get(self, key: Any) -> Any:
        with self._lock:
            if key not in self._cache:
                return None
            val, expiry = self._cache[key]
            if time.time() > expiry:
                del self._cache[key]
                return None
            return val

    def set(self, key: Any, value: Any, ttl: float = None) -> None:
        duration = ttl if ttl is not None else self.default_ttl
        expiry = time.time() + duration
        with self._lock:
            self._cache[key] = (value, expiry)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()

def memoize_with_ttl(ttl: float = 60.0) -> Callable:
    """
    Decorator to cache function results with a TTL expiration.
    """
    cache = TTLCache(default_ttl=ttl)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Generate a stable cache key for arguments
            key = (args, tuple(sorted(kwargs.items())))
            try:
                hash(key)
            except TypeError:
                # Fallback for unhashable arguments (bypass cache)
                return func(*args, **kwargs)

            cached_val = cache.get(key)
            if cached_val is not None:
                return cached_val
            
            result = func(*args, **kwargs)
            cache.set(key, result)
            return result
        return wrapper
    return decorator