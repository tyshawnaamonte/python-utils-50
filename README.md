# python-utils-50

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

python-utils-50 is a lightweight library offering fifty practical utility functions for Python developers. It focuses on solving common problems in file management, data handling, and text processing using only the standard library.

## Features

- Fifty reusable functions organized into logical modules for easy discovery
- Pure standard library implementation with no external dependencies
- Safe file handling including atomic writes and backup creation
- Text processing tools such as slug generation and duplicate removal

## Installation

```bash
pip install python-utils-50
```

To install the latest development version:

```bash
pip install git+https://github.com/Developer/python-utils-50.git
```

## Usage

```python
from python_utils_50.string_utils import slugify, remove_duplicates
from python_utils_50.file_utils import safe_write

slug = slugify("Hello World! This is a test.")
print(slug)  # "hello-world-this-is-a-test"

unique = remove_duplicates(["apple", "banana", "apple", "cherry"])
safe_write("output.txt", "Processed data", backup=True)
```