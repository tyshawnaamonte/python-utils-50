class UtilsError(Exception):
    """Base exception class for python-utils-50."""

class ConfigurationError(UtilsError):
    """Raised when utility configuration is invalid."""

class ValidationError(UtilsError):
    """Raised when data fails schema validation."""

class ExecutionError(UtilsError):
    """Raised when a process fails during execution."""

def handle_utils_exception(e: Exception) -> None:
    """
    Centralized error handling for unexpected utility failures.
    Logs the error type and returns context-aware messages.
    """
    if isinstance(e, UtilsError):
        print(f"[Utils Error] {e.__class__.__name__}: {e}")
    else:
        print(f"[Critical Error] Unexpected failure: {type(e).__name__} - {e}")

def validate_resource(data: dict) -> bool:
    """
    Validates presence of required keys in a resource dictionary.
    Raises ValidationError if keys are missing.
    """
    required = {'id', 'version'}
    if not all(key in data for key in required):
        missing = required - set(data.keys())
        raise ValidationError(f"Missing required keys: {missing}")
    return True