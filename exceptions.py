class UtilsError(Exception):
    """Base exception class for python-utils-50."""

class ConfigurationError(UtilsError):
    """Raised when configuration values are invalid or missing."""

class ProcessingError(UtilsError):
    """Raised when data transformation or core logic fails."""

def handle_exception(e: Exception) -> None:
    """Standardized logging wrapper for library exceptions."""
    if isinstance(e, UtilsError):
        print(f"[Library Error]: {e.__class__.__name__} - {str(e)}")
    else:
        print(f"[Unexpected Error]: {type(e).__name__} - {str(e)}")

def validate_resource(resource: any) -> bool:
    """Ensures resources are non-null and accessible before use."""
    if resource is None:
        raise ConfigurationError("Resource provided is None")
    return True

# Helper to wrap complex operations
def safe_execute(func, *args, **kwargs):
    """
    Executes a callable with error boundary logic
    to prevent library-level crashes.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        handle_exception(e)
        raise ProcessingError(f"Operation {func.__name__} failed") from e