"""Unit tests for calculator.py."""
import unittest

from calculator import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(8, "-", 3), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(4, "*", 3), 12)

    def test_division(self):
        self.assertEqual(calculate(9, "/", 3), 3)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "divide by zero"):
            calculate(5, "/", 0)

    def test_unsupported_operator(self):
        with self.assertRaisesRegex(ValueError, "Unsupported operator"):
            calculate(1, "^", 2)


if __name__ == "__main__":
    unittest.main()
