# Python Basics Toolkit

A beginner-friendly Python command-line calculator with input validation and unit tests. No third-party packages are required.

## Features
- Add, subtract, multiply, and divide
- Handles invalid numbers and division by zero
- Automated tests using Python's built-in `unittest`

## Requirements
- Python 3.10 or newer (3.8+ should also work)

## Run it
From this folder:

```bash
python main.py
```

Choose an operation, enter two numbers, and view the result.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
python-basics-toolkit/
├── main.py
├── calculator.py
├── tests/
│   └── test_calculator.py
├── .gitignore
└── README.md
```

Created as a small starter project for practicing Python functions, error handling, CLI input, and unit testing.
