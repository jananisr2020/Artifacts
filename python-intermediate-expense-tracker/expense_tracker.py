"""SQLite-backed expense tracking service."""
from __future__ import annotations

import csv
import sqlite3
from datetime import date
from pathlib import Path
from typing import Any


class ExpenseTracker:
    """Manage expenses stored in a SQLite database."""

    def __init__(self, database_path: str | Path = "expenses.db") -> None:
        self.database_path = str(database_path)
        self._initialize_database()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_database(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL CHECK (amount > 0),
                    category TEXT NOT NULL,
                    expense_date TEXT NOT NULL,
                    description TEXT NOT NULL DEFAULT ''
                )
                """
            )

    @staticmethod
    def _validate_amount(amount: float) -> float:
        try:
            value = float(amount)
        except (TypeError, ValueError) as exc:
            raise ValueError("Amount must be a number greater than zero.") from exc
        if value <= 0:
            raise ValueError("Amount must be greater than zero.")
        return round(value, 2)

    @staticmethod
    def _validate_date(expense_date: str) -> str:
        try:
            parsed = date.fromisoformat(expense_date)
        except (TypeError, ValueError) as exc:
            raise ValueError("Date must use YYYY-MM-DD format.") from exc
        return parsed.isoformat()

    @staticmethod
    def _validate_category(category: str) -> str:
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category cannot be empty.")
        return category.strip()

    def add_expense(
        self,
        amount: float,
        category: str,
        expense_date: str,
        description: str = "",
    ) -> int:
        amount = self._validate_amount(amount)
        category = self._validate_category(category)
        expense_date = self._validate_date(expense_date)
        description = description.strip() if isinstance(description, str) else ""

        with self._connect() as connection:
            cursor = connection.execute(
                """INSERT INTO expenses (amount, category, expense_date, description)
                   VALUES (?, ?, ?, ?)""",
                (amount, category, expense_date, description),
            )
            return int(cursor.lastrowid)

    def list_expenses(
        self,
        category: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> list[dict[str, Any]]:
        clauses: list[str] = []
        parameters: list[Any] = []

        if category:
            clauses.append("LOWER(category) = LOWER(?)")
            parameters.append(category.strip())
        if start_date:
            clauses.append("expense_date >= ?")
            parameters.append(self._validate_date(start_date))
        if end_date:
            clauses.append("expense_date <= ?")
            parameters.append(self._validate_date(end_date))

        where_clause = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        query = "SELECT * FROM expenses" + where_clause + " ORDER BY expense_date DESC, id DESC"

        with self._connect() as connection:
            rows = connection.execute(query, parameters).fetchall()
            return [dict(row) for row in rows]

    def update_expense(
        self,
        expense_id: int,
        *,
        amount: float,
        category: str,
        expense_date: str,
        description: str = "",
    ) -> bool:
        amount = self._validate_amount(amount)
        category = self._validate_category(category)
        expense_date = self._validate_date(expense_date)
        description = description.strip() if isinstance(description, str) else ""

        with self._connect() as connection:
            cursor = connection.execute(
                """UPDATE expenses
                   SET amount = ?, category = ?, expense_date = ?, description = ?
                   WHERE id = ?""",
                (amount, category, expense_date, description, expense_id),
            )
            return cursor.rowcount > 0

    def delete_expense(self, expense_id: int) -> bool:
        with self._connect() as connection:
            cursor = connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            return cursor.rowcount > 0

    def total_spending(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> float:
        clauses: list[str] = []
        parameters: list[str] = []
        if start_date:
            clauses.append("expense_date >= ?")
            parameters.append(self._validate_date(start_date))
        if end_date:
            clauses.append("expense_date <= ?")
            parameters.append(self._validate_date(end_date))
        where_clause = f" WHERE {' AND '.join(clauses)}" if clauses else ""

        with self._connect() as connection:
            row = connection.execute(
                f"SELECT COALESCE(SUM(amount), 0) AS total FROM expenses{where_clause}",
                parameters,
            ).fetchone()
            return round(float(row["total"]), 2)

    def spending_by_category(self) -> dict[str, float]:
        with self._connect() as connection:
            rows = connection.execute(
                """SELECT category, ROUND(SUM(amount), 2) AS total
                   FROM expenses GROUP BY category ORDER BY total DESC, category ASC"""
            ).fetchall()
            return {str(row["category"]): float(row["total"]) for row in rows}

    def export_csv(self, output_path: str | Path) -> int:
        expenses = self.list_expenses()
        columns = ["id", "amount", "category", "expense_date", "description"]
        with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(expenses)
        return len(expenses)
