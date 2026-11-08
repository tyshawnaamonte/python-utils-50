"""Custom exceptions for general data handling and utility operations."""


class UtilError(Exception):
    """Base exception class for all python-utils errors."""

    def __init__(self, message: str = "An unexpected utility error occurred."):
        self.message = message
        super().__init__(self.message)


class DataValidationError(UtilError):
    """Raised when data fails validation checks."""

    def __init__(self, field: str, value: object, reason: str):
        self.field = field
        self.value = value
        self.reason = reason
        message = f"Validation failed for field '{field}' with value '{value}': {reason}"
        super().__init__(message)


class DataTransformationError(UtilError):
    """Raised when converting or transforming data fails."""

    def __init__(self, source_type: str, target_type: str, details: str = ""):
        self.source_type = source_type
        self.target_type = target_type
        self.details = details
        message = f"Failed to transform data from {source_type} to {target_type}"
        if details:
            message += f": {details}"
        super().__init__(message)


class ConfigurationError(UtilError):
    """Raised when a configuration setting is invalid or missing."""

    def __init__(self, key: str, details: str = "Missing or invalid setting"):
        self.key = key
        self.details = details
        super().__init__(f"Configuration error for key '{key}': {details}")
