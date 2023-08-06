Just random useless package for testing 1

Usually, things would be under `src` directory.
But we are going to name it with the package name as this is a monorepo...?

## Installation

Run the following to install:

```python
pip install helloworld
```

## Usage

```python
from python_package_1 import random_number

# Generate random number
random_number.RandomNumberGenerator().run()
```

# Developing python_package_1

To install this, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

We are installing current package with the dev extras.
