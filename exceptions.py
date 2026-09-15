"""
Custom exception hierarchy for handling common edge cases across utilities.
"""

class PythonUtilsError(Exception):
    """Base exception class for all custom errors in the utility suite."""
    def __init__(self, message: str, error_code: str = "GENERIC_ERROR"):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"


class ValidationError(PythonUtilsError):
    """Raised when input parameters fail validation checks."""
    def __init__(self, message: str, field_name: str = None, invalid_value: object = None):
        self.field_name = field_name
        self.invalid_value = invalid_value
        suffix = f" (Field: '{field_name}' got invalid value: {invalid_value})" if field_name else ""
        super().__init__(f"{message}{suffix}", error_code="VALIDATION_ERROR")


class ConfigurationError(PythonUtilsError):
    """Raised when missing or malformed configuration blocks are detected."""
    def __init__(self, message: str, config_key: str = None):
        self.config_key = config_key
        suffix = f" (Missing or invalid key: '{config_key}')" if config_key else ""
        super().__init__(f"{message}{suffix}", error_code="CONFIGURATION_ERROR")


class ResourceUnavailableError(PythonUtilsError):
    """Raised when files, APIs, or subprocess resources cannot be accessed."""
    def __init__(self, message: str, resource_identifier: str = None, transient: bool = True):
        self.resource_identifier = resource_identifier
        self.transient = transient
        suffix = f" (Resource: '{resource_identifier}', Retryable: {transient})" if resource_identifier else ""
        super().__init__(f"{message}{suffix}", error_code="RESOURCE_UNAVAILABLE")
