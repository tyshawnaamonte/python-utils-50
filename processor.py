from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Custom exception for item validation failures."""
    pass


def validate_item(item: Any) -> Dict[str, Any]:
    """Validate an individual input item structure and content."""
    if not isinstance(item, dict):
        raise ValidationError(f"Expected dict, got {type(item).__name__}")
    
    required_keys = ["id", "name", "value"]
    missing = [key for key in required_keys if key not in item]
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")
        
    if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
        raise ValidationError("Invalid or empty item 'id'")
        
    if not isinstance(item["name"], str) or not item["name"].strip():
        raise ValidationError("Item 'name' must be a non-empty string")
        
    if not isinstance(item["value"], (int, float)) or item["value"] < 0:
        raise ValidationError("Item 'value' must be a non-negative number")
        
    return {
        "id": str(item["id"]).strip(),
        "name": item["name"].strip(),
        "value": float(item["value"])
    }


def process_batch(items: List[Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Process a batch of items with input validation in the main loop."""
    processed_items: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []

    if not isinstance(items, list):
        raise TypeError("Input payload must be a list of items")

    for index, raw_item in enumerate(items):
        try:
            validated = validate_item(raw_item)
            transformed = {
                "id": validated["id"],
                "label": validated["name"].upper(),
                "score": round(validated["value"] * 1.15, 2),
                "status": "active"
            }
            processed_items.append(transformed)
        except ValidationError as err:
            errors.append({"index": index, "item": raw_item, "error": str(err)})
        except Exception as err:
            errors.append({"index": index, "item": raw_item, "error": f"Unexpected: {err}"})

    return processed_items, errors
