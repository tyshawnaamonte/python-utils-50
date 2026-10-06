import logging
from typing import Any, Optional

# Logger setup for application errors
logger = logging.getLogger(__name__)

class BaseAppError(Exception):
    """Custom base exception for project-wide error tracking."""
    def __init__(self, message: str, code: Optional[int] = None):
        super().__init__(message)
        self.code = code

class ConfigurationError(BaseAppError):
    """Raised when project configuration is missing or invalid."""

class DataProcessingError(BaseAppError):
    """Raised during unexpected failures in core data operations."""

def handle_execution(func):
    """Decorator to catch edge case errors during function execution."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid input data in {func.__name__}: {e}")
            raise DataProcessingError(f"Input validation failed: {str(e)}")
        except Exception as e:
            logger.critical(f"Unhandled exception in {func.__name__}: {e}")
            raise
    return wrapper

def validate_not_none(value: Any, name: str) -> None:
    """Utility for checking null edge cases."""
    if value is None:
        raise ValueError(f"Parameter '{name}' cannot be None")