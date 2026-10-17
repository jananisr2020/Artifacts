"""Reusable arithmetic functions for the Python Basics Toolkit."""


def calculate(first: float, operator: str, second: float) -> float:
    """Calculate first operator second, raising ValueError for invalid operations."""
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
    }

    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second

    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}")

    return operations[operator](first, second)
