"""Batch data processing utilities for generic collection transformations."""

from typing import TypeVar, Callable, List, Iterable, Any, Dict

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    """Executes item processing in configurable chunks with optional filtering."""

    def __init__(self, batch_size: int = 100) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size: int = batch_size

    def chunk_items(self, items: Iterable[T]) -> List[List[T]]:
        """Split an iterable into lists of maximum length `batch_size`."""
        chunks: List[List[T]] = []
        current_chunk: List[T] = []

        for item in items:
            current_chunk.append(item)
            if len(current_chunk) == self.batch_size:
                chunks.append(current_chunk)
                current_chunk = []

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def map_batches(
        self, items: Iterable[T], func: Callable[[T], R], skip_errors: bool = False
    ) -> List[R]:
        """Apply a mapping function across item batches with optional error handling."""
        results: List[R] = []
        for chunk in self.chunk_items(items):
            for item in chunk:
                try:
                    results.append(func(item))
                except Exception as err:
                    if not skip_errors:
                        raise err
        return results


def process_dictionary_list(
    records: List[Dict[str, Any]], key_mapping: Dict[str, str]
) -> List[Dict[str, Any]]:
    """Rename keys in a list of dictionary records based on a mapping dictionary."""
    transformed: List[Dict[str, Any]] = []
    for record in records:
        new_record = {key_mapping.get(k, k): v for k, v in record.items()}
        transformed.append(new_record)
    return transformed
