import logging
from logging.handlers import RotatingFileHandler
import os

def setup_rotating_logger(log_file: str = "app.log", max_bytes: int = 1048576, backup_count: int = 5) -> logging.Logger:
    logger = logging.getLogger("python-utils")
    logger.setLevel(logging.INFO)

    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create rotating handler
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )

    rotating_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(rotating_handler)
    return logger

def process_items(items):
    logger = setup_rotating_logger()
    logger.info("Beginning item processing with logger rotation")
    for idx, item in enumerate(items):
        logger.debug(f"Item {idx}: {item}")
        if item > 10:
            logger.warning("Item exceeds threshold")
    logger.info("Processing finished")
    return len(items)

if __name__ == "__main__":
    result = process_items([1, 5, 12, 3, 15])
    print(f"Processed {result} items")