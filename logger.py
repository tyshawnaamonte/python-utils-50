import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str, log_file: str = 'app.log', level: int = logging.INFO) -> logging.Logger:
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure logs directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger