import logging
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class DataProcessor:
    """Batch data processor with input validation."""

    def __init__(self, required_keys: Optional[List[str]] = None) -> None:
        self.required_keys = required_keys or ["id", "payload"]

    def validate_item(self, item: Any) -> Tuple[bool, str]:
        """Validate an individual input item before processing."""
        if not isinstance(item, dict):
            return False, f"Expected dict item, got {type(item).__name__}"

        for key in self.required_keys:
            if key not in item:
                return False, f"Missing required key: {key}"
            if item[key] is None:
                return False, f"Value for key '{key}' cannot be None"

        return True, "Valid"

    def process_batch(self, items: List[Any]) -> Dict[str, Any]:
        """Process a batch of items with strict input validation in the main loop."""
        processed = []
        failed = []

        for index, item in enumerate(items):
            # Input validation step in main processing loop
            is_valid, reason = self.validate_item(item)
            if not is_valid:
                logger.warning(f"Item at index {index} skipped: {reason}")
                failed.append({"index": index, "item": item, "reason": reason})
                continue

            # Simulated payload processing
            try:
                payload_upper = str(item["payload"]).strip().upper()
                result = {"id": item["id"], "processed_payload": payload_upper}
                processed.append(result)
            except Exception as exc:
                logger.error(f"Error processing item {index}: {exc}")
                failed.append({"index": index, "item": item, "reason": str(exc)})

        return {
            "total": len(items),
            "successful_count": len(processed),
            "failed_count": len(failed),
            "results": processed,
            "errors": failed,
        }
