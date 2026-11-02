import sys
from typing import Final, Dict, Any

# Cached mapping for performance critical lookups
# Using __slots__ or frozen classes is overkill for global constants
# but maintaining a dict cache prevents repeated calculation

CACHE_SIZE_LIMIT: Final[int] = 1024
DEFAULT_TIMEOUT: Final[float] = 30.0

# Performance-optimized constant mapping for core operations
# Reduces overhead in lookup loops by pre-defining schema types
TYPE_MAP: Final[Dict[str, Any]] = {
    "int": int,
    "float": float,
    "str": str,
    "bool": bool,
    "list": list,
    "dict": dict
}

def get_system_byteorder() -> str:
    """Returns hardware byte order for serialization performance."""
    return sys.byteorder

BYTE_ORDER: Final[str] = get_system_byteorder()

# Bitwise masks for core processing logic
FLAG_ENABLED: Final[int] = 0b0001
FLAG_DEBUG: Final[int] = 0b0010
FLAG_VERBOSE: Final[int] = 0b0100

__all__ = [
    "CACHE_SIZE_LIMIT",
    "DEFAULT_TIMEOUT",
    "TYPE_MAP",
    "BYTE_ORDER",
    "FLAG_ENABLED",
    "FLAG_DEBUG",
    "FLAG_VERBOSE"
]