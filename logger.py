import logging
import sys

# Configure structured logging for the utility suite
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger('python-utils-50')

def validate_input(data: dict, required_keys: list) -> bool:
    """Ensures dictionary contains all necessary keys for processing."""
    for key in required_keys:
        if key not in data:
            logger.error(f"missing required key: {key}")
            return False
    return True

def process_main_loop(items: list):
    """Core loop processing with input validation."""
    required = ['id', 'payload']
    
    for item in items:
        if not isinstance(item, dict):
            logger.warning("skipping invalid item: non-dictionary type")
            continue
            
        if not validate_input(item, required):
            continue
            
        try:
            logger.info(f"processing item {item['id']}")
            # Processing logic follows here
        except Exception as e:
            logger.error(f"runtime error in loop: {str(e)}")

if __name__ == '__main__':
    data_queue = [{'id': 1, 'payload': 'test'}, {'invalid': 'missing_id'}]
    process_main_loop(data_queue)