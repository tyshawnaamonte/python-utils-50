class UtilityError(Exception):
    """Base exception for python-utils-50."""
    pass

class ConfigurationError(UtilityError):
    """Raised when configuration values are missing or invalid."""
    pass

class ValidationError(UtilityError):
    """Raised when input data fails validation checks."""
    pass

def safe_execute(func, *args, **kwargs):
    """Executes a function and handles common operational errors."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        raise ValidationError(f"Validation failure: {e}") from e
    except Exception as e:
        raise UtilityError(f"Unexpected utility failure: {e}") from e

# Standardized error codes for cross-module consistency
ERR_INVALID_INPUT = 1001
ERR_MISSING_CONFIG = 1002
ERR_TIMEOUT = 1003

def get_error_message(code):
    """Maps error codes to user-friendly messages."""
    messages = {
        ERR_INVALID_INPUT: "Input provided is malformed or invalid",
        ERR_MISSING_CONFIG: "Required configuration key not found",
        ERR_TIMEOUT: "Operation timed out during execution"
    }
    return messages.get(code, "An unknown error occurred")