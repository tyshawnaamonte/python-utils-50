class UtilsError(Exception):
    """Base exception for python-utils-50."""
    pass

class ValidationError(UtilsError):
    """Raised when input data fails validation."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration settings are invalid."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Check if value is None and raise exception."""
    if value is None:
        raise ValidationError(message)
    return value

def safe_execute(func, *args, **kwargs):
    """Execute function and catch custom exceptions."""
    try:
        return func(*args, **kwargs)
    except UtilsError as e:
        # Log or re-raise based on application needs
        print(f"Operation failed: {e}")
        raise