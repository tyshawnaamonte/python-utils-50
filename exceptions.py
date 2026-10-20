"""Custom exception hierarchy and standard error wrappers."""

from typing import Any, Callable, Optional, Type


class BaseUtilError(Exception):
    """Base exception for utilities with structured error details."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (details: {self.details})"
        return self.message


class ValidationError(BaseUtilError):
    """Raised when argument validation or type checking fails."""


class ConfigurationError(BaseUtilError):
    """Raised when an expected configuration key or value is invalid."""


class ProcessingError(BaseUtilError):
    """Raised when an operation fails during standard processing flow."""


def wrap_edge_case(
    func: Callable[..., Any],
    fallback_value: Any = None,
    catch: tuple[Type[BaseException], ...] = (ValueError, TypeError, KeyError),
) -> Callable[..., Any]:
    """Wraps a function to convert standard edge case errors into predictable behavior."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except catch as err:
            if fallback_value is not None:
                return fallback_value
            raise ProcessingError(
                f"Edge case encountered in {func.__name__}: {err}",
                details={"args": args, "kwargs": kwargs},
            ) from err

    return wrapper
