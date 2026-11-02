[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-50

`python-utils-50` is a lightweight, zero-dependency collection of fifty essential helper functions designed to streamline everyday Python development. From resilient retry mechanics to advanced nested dictionary manipulation, this library eliminates repetitive boilerplate across your automation scripts and backend pipelines.

## Features

* **Resilient Execution:** Built-in `@retry` decorator with configurable exponential backoff and jitter for handling transient I/O failures.
* **Deep Data Operations:** Recursively merge complex dictionaries and access nested keys safely using fluid dot-notation paths.
* **String & File Formatting:** High-performance slugifiers, secure token generators, and atomic file-writing helpers.
* **Zero External Dependencies:** Built entirely on top of the standard Python library to keep your environment lean and secure.

## Installation

Install the package via `pip`:

```bash
pip install python-utils-50
```

Or install the latest development version directly from source:

```bash
pip install git+https://github.com/Developer/python-utils-50.git
```

## Quick Start

```python
from python_utils_50 import retry, deep_merge, slugify

# 1. Clean and format strings for URLs or filenames
clean_name = slugify(" Python Utils 50: Version 1.0! ")
print(clean_name)  # Output: "python-utils-50-version-10"

# 2. Deep-merge nested configurations without overwriting parent keys
default_config = {"database": {"host": "localhost", "port": 5432}}
user_config = {"database": {"port": 5433, "ssl": True}}

final_config = deep_merge(default_config, user_config)
print(final_config)
# Output: {'database': {'host': 'localhost', 'port': 5433, 'ssl': True}}

# 3. Add auto-retry behavior to unstable operations
@retry(max_attempts=3, delay=1.0, backoff=2.0)
def connect_to_service():
    print("Attempting connection...")
    # Network call logic here
```

## License

Distributed under the MIT License. See `LICENSE` for more information.