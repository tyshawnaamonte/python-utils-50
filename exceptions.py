from typing import Optional, Any

class UtilsError(Exception):
    """Base exception class for python-utils-50."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(UtilsError):
    """Raised when configuration settings are invalid."""
    pass

class ValidationError(UtilsError):
    """Raised when input data fails validation checks."""
    def __init__(self, message: str, field: Optional[str] = None, data: Any = None) -> None:
        super().__init__(message)
        self.field = field
        self.data = data

class ProcessingError(UtilsError):
    """Raised during internal data processing cycles."""
    pass

def raise_error(message: str, error_type: type = UtilsError, **kwargs: Any) -> None:
    """Helper to raise standardized exceptions with context."""
    raise error_type(message, **kwargs)