import logging
import sys
from typing import Optional


class ColoredFormatter(logging.Formatter):
    """Custom formatter adding ANSI color codes to log levels for console output."""

    COLORS = {
        logging.DEBUG: "\033[36m",     # Cyan
        logging.INFO: "\033[32m",      # Green
        logging.WARNING: "\033[33m",   # Yellow
        logging.ERROR: "\033[31m",     # Red
        logging.CRITICAL: "\033[35m",  # Magenta
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelno, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"


def setup_logger(
    name: str = "app",
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    use_colors: bool = True,
) -> logging.Logger:
    """Configure and return a standard logger instance with formatted output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if configured multiple times
    if logger.handlers:
        return logger

    format_str = "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Console output handler
    console_handler = logging.StreamHandler(sys.stdout)
    if use_colors and sys.stdout.isatty():
        formatter = ColoredFormatter(format_str, datefmt=date_format)
    else:
        formatter = logging.Formatter(format_str, datefmt=date_format)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Optional file output handler
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_formatter = logging.Formatter(format_str, datefmt=date_format)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


def get_child_logger(parent: logging.Logger, child_name: str) -> logging.Logger:
    """Derive a child logger from an existing parent logger instance."""
    return parent.getChild(child_name)
