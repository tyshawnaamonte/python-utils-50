import logging
import sys
from typing import Optional

class CustomLogger:
    """Utility for robust application logging."""
    
    def __init__(self, name: str, log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        try:
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
            
            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
        except (PermissionError, OSError) as e:
            print(f"Critical: Failed to initialize log handler: {e}", file=sys.stderr)
            self.logger = logging.getLogger('fallback')

    def safe_log(self, message: str, level: int = logging.INFO):
        """Safely record messages without crashing execution."""
        try:
            if not isinstance(message, str):
                message = str(message)
            self.logger.log(level, message)
        except Exception as e:
            sys.stderr.write(f"Logging failure: {e}\n")

def get_logger(name: str) -> CustomLogger:
    """Factory for application-wide logging instances."""
    return CustomLogger(name)