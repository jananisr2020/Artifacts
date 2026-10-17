# Python Intermediate Project: Expense Tracker

A command-line expense tracker built with Python and SQLite. It stores data locally, supports CRUD operations, filters, summaries, and CSV export. It uses only the Python standard library.

## Features
- Add, list, update, and delete expenses
- Store expenses in a local SQLite database
- Filter expenses by category and date range
- Summarize spending by category and calculate total spending
- Export expenses to CSV
- Validate amounts and dates
- Unit tests using `unittest`

## Requirements
- Python 3.10+
- No third-party packages required

## Run the application
Open a terminal in this directory and run:

```bash
python main.py
```

The application creates `expenses.db` in the current directory on first run.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
python-intermediate-expense-tracker/
├── expense_tracker.py
├── main.py
├── tests/
│   └── test_expense_tracker.py
├── .gitignore
└── README.md
```

## Example expense fields
- Amount (must be greater than zero)
- Category (for example, Food or Transport)
- Date (YYYY-MM-DD)
- Description (optional)

This project demonstrates classes, SQLite persistence, input validation, filtering, aggregation, CSV file handling, and automated testing.
