class DataProcessingError(Exception):
    """Base exception for data handling operations."""
    pass

class ValidationError(DataProcessingError):
    """Raised when input data fails schema validation."""
    pass

class TransformationError(DataProcessingError):
    """Raised when data transformation fails."""
    pass

class ResourceNotFoundError(DataProcessingError):
    """Raised when requested resource does not exist."""
    pass

def handle_processing_error(error: Exception) -> dict:
    """Formats exceptions into a standard dictionary response."""
    return {
        "status": "error",
        "type": error.__class__.__name__,
        "message": str(error)
    }

# Helper to validate data structure presence
def validate_keys(data: dict, required_keys: list):
    """
    Ensures dictionary contains required keys.
    Raises ValidationError if any are missing.
    """
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")