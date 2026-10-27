from typing import Any, Dict, List, Optional


class ValidationError(Exception):
    """Raised when input validation fails for a payload field."""

    pass


def validate_required_fields(data: Dict[str, Any], required_keys: List[str]) -> None:
    """Check if all required keys are present and not None."""
    missing = [key for key in required_keys if key not in data or data[key] is None]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")


def validate_type(value: Any, expected_type: type, field_name: str) -> None:
    """Ensure value matches the expected python type."""
    if not isinstance(value, expected_type):
        raise ValidationError(
            f"Field '{field_name}' expected type '{expected_type.__name__}', got '{type(value).__name__}'"
        )


def validate_record(record: Dict[str, Any], schema: Dict[str, type]) -> Dict[str, Any]:
    """Validate a single data record against a simple type schema."""
    if not isinstance(record, dict):
        raise ValidationError("Record must be a dictionary")

    validate_required_fields(record, list(schema.keys()))

    for field, expected_type in schema.items():
        validate_type(record[field], expected_type, field)

    return record


def process_loop_with_validation(
    raw_items: List[Dict[str, Any]], schema: Dict[str, type]
) -> List[Dict[str, Any]]:
    """Main processing loop that validates and filters incoming data items."""
    valid_items: List[Dict[str, Any]] = []

    for item in raw_items:
        try:
            validated_item = validate_record(item, schema)
            valid_items.append(validated_item)
        except ValidationError:
            # Skip invalid item and continue loop execution
            continue

    return valid_items
