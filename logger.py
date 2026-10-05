import logging
import sys
from logging.handlers import RotatingFileHandler
from typing import Optional


def get_logger(
    name: str,
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    max_bytes: int = 1048576,  # 1MB
    backup_count: int = 5,
) -> logging.Logger:
    """Configures and retrieves a standardized logger with console and optional file output."""
    logger = logging.getLogger(name)

    # Prevent duplicate handlers if the logger is already initialized
    if logger.handlers:
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Setup stdout stream handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Setup optional rotating file handler
    if log_file:
        try:
            file_handler = RotatingFileHandler(
                log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (IOError, OSError) as err:
            # Fallback output to stdout alerting about file initialization failure
            logger.warning(
                f"Could not initialize rotating file log at '{log_file}': {err}"
            )

    return logger