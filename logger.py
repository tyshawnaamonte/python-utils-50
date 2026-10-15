import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard logger instance.

    Args:
        name: The name of the logger.
        level: The logging threshold (default INFO).

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class LoggerMixin:
    """
    Mixin class to provide logging capabilities to any class.
    """
    def __init__(self) -> None:
        self.logger: logging.Logger = get_logger(self.__class__.__name__)

    def log_info(self, message: str) -> None:
        """Log an info level message."""
        self.logger.info(message)

    def log_error(self, message: str, exc_info: bool = True) -> None:
        """Log an error level message with traceback."""
        self.logger.error(message, exc_info=exc_info)