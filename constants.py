import os
from typing import Final

# System default configurations
DEFAULT_ENCODING: Final[str] = 'utf-8'
DEFAULT_TIMEOUT: Final[int] = 30

# Directory and path defaults
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Common validation patterns
EMAIL_REGEX: Final[str] = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Environment variable keys
ENV_VAR_PREFIX: Final[str] = 'PYUTILS_'

# Default retry strategy parameters
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 0.5

def get_app_version() -> str:
    """Return the project version constant."""
    return "1.0.0"

def is_debug_mode() -> bool:
    """Check if application is running in debug mode."""
    return os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')