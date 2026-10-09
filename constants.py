"""Application constants and environment configuration utilities."""

from enum import Enum
from typing import Dict, NamedTuple


class Environment(Enum):
    """Supported application execution environments."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class TimeUnits(NamedTuple):
    """Time conversion factors represented in seconds."""

    MINUTE: int = 60
    HOUR: int = 3600
    DAY: int = 86400
    WEEK: int = 604800


# System default operational parameters
DEFAULT_TIMEOUT: int = 30
DEFAULT_RETRIES: int = 3
DEFAULT_BUFFER_SIZE: int = 8192


def get_default_headers(user_agent: str = "python-utils/1.0") -> Dict[str, str]:
    """Generate default HTTP headers for outgoing requests.

    Args:
        user_agent: Custom User-Agent header string.

    Returns:
        Dict[str, str]: Standardized HTTP header mapping.
    """
    return {
        "User-Agent": user_agent,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def is_valid_environment(env_name: str) -> bool:
    """Check if a string corresponds to a defined environment.

    Args:
        env_name: Environment identifier string to validate.

    Returns:
        bool: True if env_name is a valid environment value.
    """
    return env_name.lower() in {e.value for e in Environment}
