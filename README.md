# python-utils-50

A curated collection of high-performance Python utility functions designed to streamline repetitive coding tasks. This library focuses on simplifying data manipulation, string formatting, and file system operations with minimal dependencies.

## Features

*   **Data Transformation:** Robust decorators for type-casting and schema validation across complex nested dictionaries.
*   **File System Helpers:** Simplified context managers for recursive directory scanning and bulk file renaming.
*   **Performance Tools:** Integrated function memoization and execution time logging to optimize bottlenecks.
*   **String Sanitization:** Native support for slugifying, cleaning, and normalizing text inputs for web-safe operations.

## Installation

Install the package via `pip` from PyPI:

```bash
pip install python-utils-50
```

For development installations:

```bash
git clone https://github.com/Developer/python-utils-50.git
cd python-utils-50
pip install -e .
```

## Basic Usage

Import the desired module and utilize the optimized utility methods directly:

```python
from pyutils50 import strings, filesystem

# Slugify a string for URL usage
clean_text = strings.slugify("Hello World! This is a test.")
print(clean_text)  # output: hello-world-this-is-a-test

# List all files in a directory with specific extensions
py_files = filesystem.list_files_by_extension("./src", ".py")
print(py_files)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.