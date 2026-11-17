import os
from typing import Final

# Standard timeout intervals in seconds
DEFAULT_TIMEOUT: Final[int] = 30
SHORT_TIMEOUT: Final[int] = 5

# Common path structures
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Environment configuration keys
ENV_PREFIX: Final[str] = 'APP_'
DATABASE_URL_KEY: Final[str] = 'DATABASE_URL'
DEBUG_MODE_KEY: Final[str] = 'DEBUG'

# Supported file extensions
ALLOWED_EXTENSIONS: Final[set] = {'.json', '.csv', '.yaml', '.txt'}

# Validation constraints
MAX_RETRY_ATTEMPTS: Final[int] = 3
MIN_PASSWORD_LENGTH: Final[int] = 8

def get_app_config(key: str, default: str = '') -> str:
    """Retrieve configuration from environment variables."""
    return os.environ.get(f"{ENV_PREFIX}{key}", default)

def is_valid_extension(filename: str) -> bool:
    """Check if a file has a supported extension."""
    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)