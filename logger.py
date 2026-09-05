import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='app_logger', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for general utilities.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Rotate logs at 5MB, keep 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Also output to console for development convenience
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('logger initialization sequence complete')