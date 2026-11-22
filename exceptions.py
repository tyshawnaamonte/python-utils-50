class BaseUtilsError(Exception):
    """Base exception for python-utils-50 library."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration constraints are violated."""
    pass

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""
    pass

def handle_error(e: Exception) -> None:
    """Centralized handler for edge case logging."""
    if isinstance(e, BaseUtilsError):
        # Standard domain exceptions are logged as warnings
        print(f"Domain error occurred: {e}")
    else:
        # Unexpected exceptions are logged as critical
        print(f"Critical system error: {e}")
        raise

def validate_input(data: any, expected_type: type) -> bool:
    """Utility for strict input checking."""
    if data is None:
        raise ValidationError("Input data cannot be None")
    if not isinstance(data, expected_type):
        raise ValidationError(f"Expected {expected_type.__name__}, got {type(data).__name__}")
    return True