import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute a function with standardized error handling."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Invalid argument type: {e}")
    except ValueError as e:
        logger.error(f"Invalid value provided: {e}")
    except Exception as e:
        logger.critical(f"Unexpected execution failure: {e}", exc_info=True)
    return default

def validate_input(data: Any, expected_type: type) -> bool:
    """Verify data integrity and type constraints."""
    if data is None:
        logger.warning("Validation failed: data is None")
        return False
    
    if not isinstance(data, expected_type):
        logger.warning(f"Validation failed: expected {expected_type}, got {type(data)}")
        return False
    
    return True

class ExecutionContext:
    """Resource manager for controlled process execution."""
    def __init__(self, name: str):
        self.name = name

    def run(self, action: Callable, payload: Any) -> Optional[Any]:
        if not validate_input(payload, dict):
            return None
        return safe_execute(action, payload)