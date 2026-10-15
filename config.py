import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load JSON config with fallback to defaults."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persist current configuration to disk."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    # usage example
    defaults = {'port': 8080, 'debug': False}
    current_cfg = load_config('settings.json', defaults)
    print(f'Loaded configuration: {current_cfg}')