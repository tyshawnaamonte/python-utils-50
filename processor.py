from typing import Any, Dict, List, Optional, Tuple


class ProcessingError(Exception):
    """Custom exception raised when item processing fails validation or execution."""
    pass


def validate_input_item(item: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate an individual data payload before processing."""
    if not isinstance(item, dict):
        return False, f"Expected dict, got {type(item).__name__}"

    if "id" not in item or not isinstance(item["id"], (int, str)):
        return False, "Missing or invalid 'id' field"

    if "action" not in item or not isinstance(item["action"], str):
        return False, "Missing or invalid 'action' field"

    if "payload" in item and not isinstance(item["payload"], (dict, list)):
        return False, "'payload' must be a dict or list if provided"

    return True, None


def process_item_batch(batch: List[Dict[str, Any]], ignore_errors: bool = True) -> List[Dict[str, Any]]:
    """
    Main processing loop that validates and processes a batch of inputs.
    """
    results = []

    for idx, raw_item in enumerate(batch):
        # Validate input schema before processing
        is_valid, error_msg = validate_input_item(raw_item)
        if not is_valid:
            err_details = f"Item at index {idx} failed validation: {error_msg}"
            if not ignore_errors:
                raise ProcessingError(err_details)
            results.append({
                "status": "skipped",
                "error": err_details,
                "item_id": raw_item.get("id") if isinstance(raw_item, dict) else None
            })
            continue

        # Execute processing logic for valid inputs
        item_id = raw_item["id"]
        action = raw_item["action"].lower()
        payload = raw_item.get("payload", {})

        processed_data = {
            "status": "success",
            "item_id": item_id,
            "result": f"Executed '{action}' successfully",
            "details": payload
        }
        results.append(processed_data)

    return results
