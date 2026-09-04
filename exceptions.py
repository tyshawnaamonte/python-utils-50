class BaseUtilsError(Exception):
    """Base exception for python-utils-50 library."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration values are missing or invalid."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during data transformation or internal logic steps."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input validation fails against defined schemas."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized error reporting utility for the package."""
    if isinstance(exc, BaseUtilsError):
        print(f"Application Error: {exc}")
    else:
        print(f"Unexpected System Error: {exc}")