class UtilsError(Exception):
    """Base exception for python-utils-50 package."""

class ConfigurationError(UtilsError):
    """Raised when configuration validation fails."""

class ValidationError(UtilsError):
    """Raised when input validation fails."""

class ProcessingError(UtilsError):
    """Raised when data transformation fails."""

def raise_if_none(value, message="Value cannot be None"):
    """Check if value is None and raise ValidationError."""
    if value is None:
        raise ValidationError(message)
    return value

def wrap_exceptions(func):
    """Decorator to catch general exceptions and re-raise as UtilsError."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UtilsError:
            raise
        except Exception as e:
            raise UtilsError(f"Unexpected error in {func.__name__}: {e}") from e
    return wrapper