import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standard logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_execution_time(logger: logging.Logger, func_name: str, elapsed: float) -> None:
    """Utility to log execution duration of a function."""
    logger.info(f"Function '{func_name}' completed in {elapsed:.4f} seconds")

def format_exception(e: Exception) -> str:
    """Utility to standardize exception string formatting."""
    return f"{type(e).__name__}: {str(e)}"

# Global default logger instance
default_logger = get_logger("python-utils-50")