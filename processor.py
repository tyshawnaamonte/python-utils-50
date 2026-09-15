from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles transformation and validation of input datasets."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize processor with optional configuration settings."""
        self.settings = settings or {}

    def clean_records(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Removes empty values and trims whitespace from string fields."""
        cleaned = []
        for entry in data:
            processed = {
                k: v.strip() if isinstance(v, str) else v 
                for k, v in entry.items() if v is not None
            }
            cleaned.append(processed)
        return cleaned

    def transform_keys(self, data: List[Dict[str, Any]], mapping: Dict[str, str]) -> List[Dict[str, Any]]:
        """Maps old dictionary keys to new values provided in mapping."""
        transformed = []
        for entry in data:
            new_entry = {mapping.get(k, k): v for k, v in entry.items()}
            transformed.append(new_entry)
        return transformed

    def validate_batch(self, data: List[Dict[str, Any]], required_keys: List[str]) -> bool:
        """Checks if all required keys exist in every record of the batch."""
        return all(all(key in record for key in required_keys) for record in data)