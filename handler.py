"""Task and execution handler utilities for robust operations."""

import time
from typing import Any, Callable, Dict, Optional, TypeVar

T = TypeVar("T")


class TaskHandler:
    """Handles execution of callables with retry logic and fallback mechanisms."""

    def __init__(self, max_retries: int = 3, delay: float = 1.0) -> None:
        """Initialize the handler with default retry configuration."""
        self.max_retries = max_retries
        self.delay = delay
        self._execution_stats: Dict[str, int] = {"success": 0, "failed": 0}

    def execute(
        self,
        func: Callable[..., T],
        *args: Any,
        fallback: Optional[T] = None,
        **kwargs: Any,
    ) -> Optional[T]:
        """Execute a callable with retry handling and optional fallback value.

        Args:
            func: The function to execute.
            *args: Positional arguments for the function.
            fallback: Default value returned if all retries fail.
            **kwargs: Keyword arguments for the function.

        Returns:
            The function result if successful, otherwise the fallback value.
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                result = func(*args, **kwargs)
                self._execution_stats["success"] += 1
                return result
            except Exception:
                if attempt < self.max_retries:
                    time.sleep(self.delay)
                else:
                    self._execution_stats["failed"] += 1

        return fallback

    def get_stats(self) -> Dict[str, int]:
        """Retrieve execution statistics for the handler instance."""
        return self._execution_stats.copy()
