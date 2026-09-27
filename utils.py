import os
import logging
from typing import Any, List, Optional

# Configure standard logging for utility operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback default."""
    return os.environ.get(key, default) or ""

def filter_none_values(data: dict) -> dict:
    """Remove keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]

class DataProcessor:
    """Base class for data manipulation tasks."""
    def __init__(self, items: List[Any]):
        self.items = items

    def process_and_clean(self) -> List[Any]:
        """Standardizes internal list by removing empty entries."""
        return [item for item in self.items if item]

if __name__ == "__main__":
    # Example usage for verification
    processor = DataProcessor(["a", "", "b", None, "c"])
    logger.info(f"Processed result: {processor.process_and_clean()}")