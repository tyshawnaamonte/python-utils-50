import logging
import sys
from typing import Optional

def get_configured_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger instance with standard formatting.
    """
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

def log_execution_context(logger: logging.Logger, func_name: str, status: str) -> None:
    """
    Standardized log message for function lifecycle events.
    """
    logger.info(f"Execution of {func_name} reached status: {status}")

def setup_basic_logging(level: int = logging.INFO) -> None:
    """
    Global configuration for application-wide logging.
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )