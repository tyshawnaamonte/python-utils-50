from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles transformation of dictionary lists into formatted records."""

    def __init__(self, target_key: str = "id") -> None:
        self.target_key = target_key

    def process_batch(self, data: List[Dict[str, Any]]) -> Dict[Any, Dict[str, Any]]:
        """
        Organizes a list of dictionaries into a lookup table.

        Args:
            data: A list of dictionaries containing keys to be indexed.

        Returns:
            A dictionary mapping target keys to record objects.
        """
        return {item[self.target_key]: item for item in data if self.target_key in item}

    def get_summary(self, data: List[Dict[str, Any]]) -> Dict[str, int]:
        """
        Calculates the frequency of target keys in the provided data.

        Args:
            data: List of data dictionaries.

        Returns:
            A summary dictionary with counts of occurrences.
        """
        summary: Dict[Any, int] = {}
        for item in data:
            key = item.get(self.target_key)
            if key is not None:
                summary[key] = summary.get(key, 0) + 1
        return summary