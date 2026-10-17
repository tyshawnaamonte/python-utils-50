import logging
from typing import Any, Dict, List, Union

logger = logging.getLogger(__name__)

def validate_input_schema(data: Any, required_fields: List[str]) -> bool:
    """Ensures input dictionary contains mandatory keys."""
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dict")
        return False

    missing = [field for field in required_fields if field not in data]
    if missing:
        logger.error(f"Missing required fields: {', '.join(missing)}")
        return False
    return True

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null entries and strips whitespace from strings."""
    sanitized = {}
    for key, value in payload.items():
        if value is None:
            continue
        if isinstance(value, str):
            sanitized[key] = value.strip()
        else:
            sanitized[key] = value
    return sanitized

def process_data_batch(batch: List[Dict[str, Any]], required: List[str]) -> List[Dict[str, Any]]:
    """Main loop validation logic for data processing."""
    valid_items = []
    for item in batch:
        if validate_input_schema(item, required):
            valid_items.append(sanitize_payload(item))
    return valid_items