class BaseUtilsError(Exception):
    """Base exception for python-utils-50 library."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration values are invalid."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during core utility processing failures."""
    pass

def handle_exception(exc: Exception) -> None:
    """Standardized exception logging and re-raising."""
    if isinstance(exc, BaseUtilsError):
        # In a real scenario, integrate with project logger
        print(f"[ERROR] {type(exc).__name__}: {exc}")
    else:
        print(f"[CRITICAL] Unexpected error: {exc}")
    raise exc

def validate_input(value: any, expected_type: type) -> None:
    """Checks input types and raises structured exceptions."""
    if not isinstance(value, expected_type):
        raise ValidationError(f"Expected {expected_type.__name__}, got {type(value).__name__}")