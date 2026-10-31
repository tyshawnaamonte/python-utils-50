import math
from typing import Any, Dict, List, Optional


class ProcessingError(Exception):
    """Custom exception raised when batch record processing encounters unrecoverable errors."""
    pass


class BatchProcessor:
    """Processes and sanitizes structured batch data with edge-case handling."""

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode

    def safe_divide(self, numerator: Any, denominator: Any, default: float = 0.0) -> float:
        """Safely divides two numeric inputs, handling zero division, nan, and type conversion."""
        try:
            num = float(numerator)
            den = float(denominator)
            if den == 0.0 or math.isnan(num) or math.isnan(den) or math.isinf(num) or math.isinf(den):
                return default
            return num / den
        except (ValueError, TypeError) as err:
            if self.strict_mode:
                raise ProcessingError(f"Invalid numeric inputs: {numerator}, {denominator}") from err
            return default

    def sanitize_record(self, record: Any) -> Dict[str, Any]:
        """Normalizes dictionary values and handles malformed data types."""
        if not isinstance(record, dict):
            if self.strict_mode:
                raise ProcessingError(f"Expected dict, got {type(record).__name__}")
            return {}

        clean_record = {}
        for key, value in record.items():
            str_key = str(key) if not isinstance(key, str) else key
            
            if value is None:
                clean_record[str_key] = ""
            elif isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                clean_record[str_key] = 0.0
            elif isinstance(value, (int, float)):
                clean_record[str_key] = round(float(value), 4)
            elif isinstance(value, (list, tuple, set)):
                clean_record[str_key] = [v for v in value if v is not None]
            else:
                clean_record[str_key] = str(value)

        return clean_record

    def process_batch(self, batch: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Processes a list of records while trapping bad data elements."""
        if batch is None:
            return []

        if not isinstance(batch, (list, tuple)):
            if self.strict_mode:
                raise ProcessingError(f"Invalid batch payload type: {type(batch).__name__}")
            return []

        results = []
        for item in batch:
            try:
                cleaned = self.sanitize_record(item)
                if cleaned:
                    results.append(cleaned)
            except ProcessingError:
                if self.strict_mode:
                    raise
                continue
            except Exception as err:
                if self.strict_mode:
                    raise ProcessingError(f"Unexpected processing failure: {err}") from err
                continue

        return results
