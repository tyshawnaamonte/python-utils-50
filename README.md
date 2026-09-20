# python-utils-50

A curated collection of production-ready Python utility functions designed to streamline repetitive development tasks. This library focuses on performance, type-safety, and minimal dependencies for everyday engineering needs.

## Features

*   **Data Transformation**: Robust helpers for nested dictionary flattening and complex list manipulations.
*   **Timezone-Aware Helpers**: Simplified formatting and parsing tools for UTC-based timestamp conversions.
*   **FileSystem Shortcuts**: Context managers for recursive directory cleanup and path validation.
*   **Functional Decorators**: Lightweight decorators for request retries, execution timing, and silent exception handling.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-50
```

## Basic Usage

Quickly leverage the library to manage file paths or handle dictionary operations in your data pipelines:

```python
from pyutils50.file_ops import safe_mkdir
from pyutils50.data import flatten_dict

# Ensure a directory exists
safe_mkdir("./logs/archives")

# Flatten deeply nested API responses
raw_data = {"user": {"id": 1, "meta": {"login": "admin"}}}
clean_data = flatten_dict(raw_data, separator="_")

print(clean_data)
# Output: {'user_id': 1, 'user_meta_login': 'admin'}
```

## Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request if you have utility functions that would benefit the community.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.