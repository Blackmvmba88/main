# Simple Calculator

A Python-based calculator application providing basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling)
- Power/Exponentiation

## Usage

### Interactive Mode

Run the calculator in interactive mode:

```bash
python calculator.py
```

### As a Module

Import and use the calculator functions in your own code:

```python
from calculator import add, subtract, multiply, divide, power

result = add(5, 3)  # Returns 8
result = divide(10, 2)  # Returns 5.0
result = power(2, 3)  # Returns 8
```

## Running Tests

Run the test suite using unittest:

```bash
python -m unittest test_calculator.py
```

Or run tests with verbose output:

```bash
python -m unittest test_calculator.py -v
```

## Requirements

- Python 3.6 or higher

## Error Handling

The calculator includes proper error handling:
- Division by zero raises a `ValueError`
- Invalid inputs are caught and reported to the user
