import functools
from typing import Callable, Any, Dict

_CACHE_SIZE = 1024

# Lru cache for validator results to reduce computation overhead
# on recurring validation requests in the core module.
@functools.lru_cache(maxsize=_CACHE_SIZE)
def validate_schema(data: tuple, schema: tuple) -> bool:
    """Validates input data against a provided schema structure."""
    if len(data) != len(schema):
        return False
    return all(isinstance(d, s) for d, s in zip(data, schema))

class DataValidator:
    """Core validator utilizing memoization for performance optimization."""
    def __init__(self):
        self._memo = {}

    def check(self, payload: Dict[str, Any], schema: Dict[str, type]) -> bool:
        """Converts dictionary to hashable items for cached validation."""
        items = tuple(sorted(payload.items()))
        types = tuple(sorted(schema.items()))
        return validate_schema(items, types)

# Global validator instance for performance sharing
validator = DataValidator()

def quick_check(data: Dict, schema: Dict) -> bool:
    """Practical entry point for high-speed validation."""
    return validator.check(data, schema)