import re
from typing import Any, Dict, Union


class ValidationError(ValueError):
    """Custom exception raised when data validation fails."""

    pass


class DataValidator:
    """Utility class to validate input payloads in the main processing loop."""

    @staticmethod
    def validate_record(
        record: Dict[str, Any], required_fields: Dict[str, type]
    ) -> None:
        """Validates a dictionary record against specified field names and types.

        Raises ValidationError if verification fails.
        """
        if not isinstance(record, dict):
            raise ValidationError(
                f"Record must be a dictionary, got {type(record).__name__}"
            )

        for field, expected_type in required_fields.items():
            if field not in record:
                raise ValidationError(
                    f"Missing required field: '{field}'"
                )

            val = record[field]
            if not isinstance(val, expected_type):
                raise ValidationError(
                    f"Field '{field}' expected type {expected_type.__name__}, got {type(val).__name__}"
                )

    @staticmethod
    def validate_numeric_range(
        value: Union[int, float],
        min_val: Union[int, float, None] = None,
        max_val: Union[int, float, None] = None,
    ) -> None:
        """Ensures a numerical value is within specified bounds."""
        if not isinstance(value, (int, float)):
            raise ValidationError(
                f"Value must be a number, got {type(value).__name__}"
            )

        if min_val is not None and value < min_val:
            raise ValidationError(
                f"Value {value} is below the limit of {min_val}"
            )

        if max_val is not None and value > max_val:
            raise ValidationError(
                f"Value {value} is above the limit of {max_val}"
            )
