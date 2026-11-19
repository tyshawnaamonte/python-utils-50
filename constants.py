import os
from typing import Final

# Standard environmental constants for application configuration
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'

# File system and path constants
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Application-wide MIME types and common headers
DEFAULT_HEADERS: Final[dict] = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Thresholds for data processing
CHUNK_SIZE: Final[int] = 1024 * 1024  # 1MB
BUFFER_SIZE: Final[int] = 4096

# Boolean configuration flags
DEBUG_MODE: Final[bool] = os.getenv('DEBUG', 'False').lower() == 'true'
ENABLE_CACHING: Final[bool] = True

# Error and status messages
SUCCESS_MESSAGE: Final[str] = 'Operation completed successfully'
ERROR_MESSAGE: Final[str] = 'An unexpected error occurred'