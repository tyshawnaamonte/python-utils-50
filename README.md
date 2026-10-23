# python-utils-50

A curated collection of production-ready Python utility functions designed to streamline repetitive coding tasks. This library focuses on performance, readability, and minimizing boilerplate code in daily scripting and enterprise projects.

## Features

*   **Data Validation:** Robust decorators and schemas for rapid input sanitization and type checking.
*   **File System Helpers:** Simplified context managers for recursive directory traversing and bulk file processing.
*   **Performance Benchmarking:** Intuitive decorators to measure and log function execution time in production logs.
*   **String Formatting:** Optimized utilities for handling complex regex-based replacements and text cleaning workflows.

## Installation

Install the package via pip:

```bash
pip install python-utils-50
```

To install from source for local development:

```bash
git clone https://github.com/Developer/python-utils-50.git
cd python-utils-50
pip install -e .
```

## Usage

Import the required utilities to handle common boilerplate tasks with clean, readable code.

```python
from pyutils import time_it, slugify

# Use the benchmarking decorator to monitor function performance
@time_it
def process_data(data):
    return [d.upper() for d in data]

# Clean strings for URL-friendly naming conventions
raw_text = "Hello World: Utilities Edition!"
cleaned = slugify(raw_text)

print(f"Slug: {cleaned}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.