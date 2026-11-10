from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception class for all utils library errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(BaseUtilsError):
    """Raised when the provided configuration is invalid."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when data validation fails during processing."""
    def __init__(self, message: str, target: Any = None) -> None:
        super().__init__(message)
        self.target = target

class ProcessingError(BaseUtilsError):
    """Raised when an unexpected error occurs during data transformation."""
    pass

def raise_if_none(value: Optional[Any], name: str) -> None:
    """Utility to raise a validation error if the provided value is None."""
    if value is None:
        raise ValidationError(f"Required parameter '{name}' cannot be None")

def format_error_msg(error: Exception) -> str:
    """Helper to format exception details into a readable string."""
    return f"{error.__class__.__name__}: {str(error)}"