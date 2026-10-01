# python-utils-50

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`python-utils-50` is a curated collection of fifty micro-utilities designed to eliminate boilerplate code in everyday Python projects. From robust nested dictionary merging to safe directory creation, this library provides highly optimized, zero-dependency helpers that streamline your development workflow.

## Features

* **Type-Safe Deep Merging**: Recursively combine nested dictionaries without side effects or mutating the original structures.
* **Resilient File I/O**: Safe wrapper functions that automatically handle and generate missing nested directories during file write operations.
* **Smart Datetime Parsing**: Out-of-the-box parsing for fifty common string-based timestamp formats directly into standard Python datetime objects.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-50
```

## Usage

Here is a quick example of how to merge configurations and write the output safely:

```python
from python_utils_50.dicts import deep_merge
from python_utils_50.files import safe_write

# Combine nested configuration dictionaries
default_config = {"server": {"host": "127.0.0.1", "port": 80}}
user_config = {"server": {"port": 8080}}
final_config = deep_merge(default_config, user_config)

# Output the result, automatically creating any missing parent directories
safe_write("config/prod/settings.json", str(final_config))
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.