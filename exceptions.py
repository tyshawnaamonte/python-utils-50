from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception class for python-utils-50 library."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    def __init__(self, message: str, context: Optional[Any] = None) -> None:
        super().__init__(message)
        self.context = context

class ConfigurationError(BaseUtilsError):
    """Raised when environment or configuration is invalid."""
    def __init__(self, message: str, key: Optional[str] = None) -> None:
        super().__init__(message)
        self.key = key

class ExecutionError(BaseUtilsError):
    """Raised when a process fails during execution."""
    def __init__(self, message: str, exit_code: int = 1) -> None:
        super().__init__(message)
        self.exit_code = exit_code

def raise_if_none(value: Any, name: str) -> None:
    """Validates that a variable is not None, raising ValidationError if so."""
    if value is None:
        raise ValidationError(f"Variable '{name}' cannot be None")