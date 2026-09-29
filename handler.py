import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataHandler:
    """Manages data processing and transformation lifecycle."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.storage: Dict[str, Any] = {}

    def process_item(self, key: str, value: Any) -> bool:
        """Validates and stores individual data items."""
        if not key or not isinstance(key, str):
            logger.error("Invalid key provided: %s", key)
            return False
            
        self.storage[key] = value
        logger.info("Processed key: %s", key)
        return True

    def get_all(self) -> Dict[str, Any]:
        """Returns current state of storage."""
        return self.storage

    def clear_storage(self) -> None:
        """Resets the handler state."""
        self.storage.clear()
        logger.info("Handler storage cleared")

def initialize_handler(config: Dict[str, Any]) -> DataHandler:
    """Factory method for handler instantiation."""
    return DataHandler(config=config)