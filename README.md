# python-utils-50

A curated collection of high-performance utility functions and helper classes designed to streamline repetitive Python development tasks. This library focuses on clean, dependency-free code to improve maintainability across various projects.

## Features

*   **FileSystem Streamline:** Simplify recursive directory traversal and complex path manipulations with intuitive one-line wrappers.
*   **Data Transformation:** Efficiently convert nested dictionaries to dot-notation objects and handle complex JSON serialization edge cases.
*   **Time Utilities:** Robust wrappers for timestamp conversion, timezone-aware interval calculations, and execution benchmarking decorators.
*   **Validation Helpers:** Lightweight schema checking and email/URL format sanitizers to minimize boilerplate input validation.

## Installation

Install the package via pip:

```bash
pip install python-utils-50
```

For development mode and access to the testing suite:

```bash
git clone https://github.com/Developer/python-utils-50.git
cd python-utils-50
pip install -r requirements.txt
```

## Usage

Here is a quick example of how to use the execution timer decorator to profile your functions:

```python
from pyutils.time import timer

@timer
def process_data(items):
    # Simulate an intensive task
    return [i**2 for i in range(items)]

# The execution time will be automatically logged to console
process_data(100000)
```

For advanced usage, refer to the [documentation](https://github.com/Developer/python-utils-50/wiki) for full module specifications.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.