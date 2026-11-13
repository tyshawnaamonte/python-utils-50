import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard logger instance.

    Args:
        name: The name of the logger.
        level: The logging threshold level.

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

def log_exception(logger: logging.Logger, message: str, exc: Exception) -> None:
    """
    Logs an exception with an associated message.

    Args:
        logger: The logger instance to use.
        message: Contextual information about the error.
        exc: The exception object being logged.
    """
    logger.error(f"{message}: {str(exc)}", exc_info=True)

class CustomAdapter(logging.LoggerAdapter):
    """
    An adapter for injecting contextual information into log messages.
    """
    def process(self, msg: str, kwargs: dict) -> tuple[str, dict]:
        return f"[{self.extra['context']}] {msg}", kwargs