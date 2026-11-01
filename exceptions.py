"""Custom exception hierarchy for general data handling utilities."""

from typing import Any, Dict, Optional


class DataUtilsError(Exception):
    """Base exception for all errors raised by the data utils library."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            detail_str = ", ".join(f"{k}={v!r}" for k, v in self.details.items())
            return f"{self.message} ({detail_str})"
        return self.message


class ValidationError(DataUtilsError):
    """Raised when data fails validation checks against expected schemas or rules."""

    pass


class TransformationError(DataUtilsError):
    """Raised when data transformation, parsing, or casting operations fail."""

    pass


class ConfigurationError(DataUtilsError):
    """Raised when invalid options or environment settings are supplied."""

    pass


class ResourceNotFoundError(DataUtilsError):
    """Raised when a specified key, file, or data structure is missing."""

    pass
