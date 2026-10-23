"""Custom exception classes and edge case handlers for general utilities."""

from typing import Any, Callable, Dict, Optional, Type
import functools


class BaseUtilError(Exception):
    """Base exception class for python-utils with context logging."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert exception state into a plain dictionary."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(BaseUtilError):
    """Raised when input validation encounters an unexpected edge case."""
    pass


class ProcessingError(BaseUtilError):
    """Raised when operation or data transformation fails unexpectedly."""
    pass


class ResourceAccessError(BaseUtilError):
    """Raised when accessing or reading resource utilities fails."""
    pass


def safe_execute(
    default_return: Any = None,
    target_exception: Type[BaseUtilError] = ProcessingError,
    reraise: bool = True,
) -> Callable:
    """Decorator that wraps functions to handle unhandled edge cases gracefully."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except BaseUtilError:
                raise
            except Exception as err:
                if not reraise:
                    return default_return
                context = {"func": func.__name__, "args": str(args), "kwargs": str(kwargs)}
                raise target_exception(
                    f"Unhandled error in {func.__name__}: {str(err)}", details=context
                ) from err

        return wrapper

    return decorator
