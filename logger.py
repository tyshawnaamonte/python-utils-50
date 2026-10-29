import logging
import sys
from typing import Optional

class Logger:
    """Centralized application logging utility."""
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._configure_handlers()

    def _configure_handlers(self) -> None:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = True) -> None:
        self.logger.error(msg, exc_info=exc_info)

    @classmethod
    def get_logger(cls, name: str, level: int = logging.INFO) -> 'Logger':
        return cls(name, level)

def setup_default_logger(name: str = 'python-utils-50') -> Logger:
    return Logger(name)