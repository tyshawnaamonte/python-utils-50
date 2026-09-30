import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> Optional[dict]:
    """Validates input structure and required fields."""
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dict")
        return None
    
    required = ['id', 'action']
    for key in required:
        if key not in data:
            logger.error(f"Missing required field: {key}")
            return None
            
    if not isinstance(data['id'], int) or data['id'] < 0:
        logger.error("Invalid id format: must be positive integer")
        return None
        
    return data

def process_items(items: list):
    """Main processing loop with validation."""
    for item in items:
        validated = validate_payload(item)
        if not validated:
            continue
            
        try:
            print(f"Processing item {validated['id']}: {validated['action']}")
        except Exception as e:
            logger.exception(f"Unexpected error processing item {item.get('id')}: {e}")