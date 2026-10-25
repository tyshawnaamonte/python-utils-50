import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: str = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
    formatter_str: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a logger instance with console and rotating file output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    if formatter_str is None:
        formatter_str = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"

    formatter = logging.Formatter(formatter_str)

    # Ensure target directory exists if a path is specified
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Setup file handler with log rotation
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Setup standard console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    # Example usage demonstration
    app_logger = setup_logger("demo", "logs/app.log", logging.DEBUG)
    app_logger.info("Logger successfully initialized with rotation")
    app_logger.debug("Debug log entry generated")
