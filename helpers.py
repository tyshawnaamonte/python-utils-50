import logging

logger = logging.getLogger(__name__)

def validate_input(data):
    """Validates dictionary structure for processing."""
    required_fields = {'id', 'payload'}
    if not isinstance(data, dict):
        return False
    if not required_fields.issubset(data.keys()):
        return False
    if not isinstance(data['id'], int):
        return False
    return True

def run_processing_loop(items):
    """Main processing loop with input validation."""
    processed = []
    for item in items:
        if not validate_input(item):
            logger.warning(f"skipping invalid item: {item}")
            continue
        
        try:
            # Simulate core logic
            result = item['payload'].upper()
            processed.append({'id': item['id'], 'result': result})
        except Exception as e:
            logger.error(f"processing error for item {item.get('id')}: {e}")
            
    return processed

if __name__ == "__main__":
    data_stream = [
        {'id': 1, 'payload': 'test'},
        {'id': 'invalid', 'payload': 'oops'},
        {'id': 2, 'payload': 'data'}
    ]
    results = run_processing_loop(data_stream)
    print(f"processed {len(results)} items")