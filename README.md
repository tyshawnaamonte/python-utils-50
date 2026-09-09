[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-50

`python-utils-50` is a curated collection of fifty highly efficient, zero-dependency Python utility functions designed to streamline daily development workflows. From advanced dictionary manipulation to robust file-system operations, this library eliminates repetitive boilerplate code so you can focus on building core features.

## Features

* **High-Performance Data Flattening:** Recursively flatten deeply nested dictionaries and lists with custom delimiters in a single pass.
* **Smart File I/O:** Safely read and write JSON, YAML, and CSV files with automatic encoding detection and directory creation.
* **Time & Date Helpers:** Convert timestamps to human-readable durations and parse ISO dates without external dependencies.
* **Resilient Network Retries:** A lightweight decorator to automatically retry failing HTTP requests or database connections with exponential backoff.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-50
```

## Quick Start

```python
from python_utils_50.data import flatten_dict
from python_utils_50.decorators import retry

# 1. Flatten a complex nested dictionary
nested_data = {
    "user": {
        "profile": {
            "name": "Alice",
            "role": "Lead Engineer"
        }
    }
}
flat_data = flatten_dict(nested_data, separator=".")
print(flat_data)
# Output: {'user.profile.name': 'Alice', 'user.profile.role': 'Lead Engineer'}


# 2. Retry a flaky network function with exponential backoff
@retry(retries=3, delay=2.0)
def fetch_api_status():
    print("Attempting to connect to the server...")
    # Simulated API call logic here
    return "Success"

fetch_api_status()
```

## License

This project is licensed under the MIT License.