"""Unit tests for the SQLite-backed expense tracker."""
import csv
import tempfile
import unittest
from pathlib import Path

from expense_tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.database = Path(self.temp_dir.name) / "test_expenses.db"
        self.csv_path = Path(self.temp_dir.name) / "expenses.csv"
        self.tracker = ExpenseTracker(self.database)

    def add_sample_expenses(self):
        self.tracker.add_expense(120, "Food", "2026-10-01", "Lunch")
        self.tracker.add_expense(80.50, "Transport", "2026-10-02", "Bus")
        self.tracker.add_expense(50, "Food", "2026-10-03", "Coffee")

    def test_add_and_list_expenses(self):
        expense_id = self.tracker.add_expense(120, "Food", "2026-10-01", "Lunch")
        items = self.tracker.list_expenses()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], expense_id)
        self.assertEqual(items[0]["amount"], 120.0)

    def test_invalid_amount_is_rejected(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense(0, "Food", "2026-10-01")

    def test_invalid_date_is_rejected(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense(10, "Food", "01-10-2026")

    def test_filter_by_category(self):
        self.add_sample_expenses()
        items = self.tracker.list_expenses(category="food")
        self.assertEqual(len(items), 2)

    def test_update_and_delete(self):
        expense_id = self.tracker.add_expense(10, "Food", "2026-10-01")
        self.assertTrue(self.tracker.update_expense(
            expense_id, amount=25, category="Books",
            expense_date="2026-10-02", description="Notebook"
        ))
        self.assertEqual(self.tracker.list_expenses()[0]["category"], "Books")
        self.assertTrue(self.tracker.delete_expense(expense_id))
        self.assertEqual(self.tracker.list_expenses(), [])

    def test_summary(self):
        self.add_sample_expenses()
        self.assertEqual(self.tracker.total_spending(), 250.5)
        self.assertEqual(self.tracker.spending_by_category(), {"Food": 170.0, "Transport": 80.5})

    def test_csv_export(self):
        self.add_sample_expenses()
        count = self.tracker.export_csv(self.csv_path)
        self.assertEqual(count, 3)
        with self.csv_path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        self.assertEqual(len(rows), 3)
        self.assertIn("category", rows[0])


if __name__ == "__main__":
    unittest.main()
