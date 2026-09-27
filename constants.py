import os
from typing import Final

# Application path configurations
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Processing constraints
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
CHUNK_SIZE: Final[int] = 4096

# Formatting defaults
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
ENCODING: Final[str] = 'utf-8'

# Status codes for internal handlers
STATUS_SUCCESS: Final[int] = 200
STATUS_ERROR: Final[int] = 500

def get_environment_config() -> dict:
    """Retrieve base configuration settings from environment."""
    return {
        "timeout": int(os.getenv("APP_TIMEOUT", DEFAULT_TIMEOUT)),
        "debug": os.getenv("APP_DEBUG", "False") == "True"
    }