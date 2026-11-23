from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception class for all python-utils-50 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(BaseUtilsError):
    """Raised when the utility configuration is invalid."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised when data processing operations fail."""
    def __init__(self, message: str, context: Any = None) -> None:
        super().__init__(message)
        self.context = context

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    pass

def raise_if_none(value: Any, name: str) -> None:
    """Ensure value is not None or raise ValidationError."""
    if value is None:
        raise ValidationError(f"Required parameter '{name}' cannot be None")