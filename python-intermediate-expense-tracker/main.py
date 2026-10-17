"""Command-line interface for the expense tracker."""
from datetime import date
from expense_tracker import ExpenseTracker


def ask_date(prompt: str, default_today: bool = False) -> str:
    default = date.today().isoformat()
    while True:
        value = input(f"{prompt} [{default if default_today else 'YYYY-MM-DD'}]: ").strip()
        if not value and default_today:
            return default
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def main() -> None:
    tracker = ExpenseTracker()
    menu = """
Expense Tracker
1. Add expense
2. List expenses
3. Update expense
4. Delete expense
5. Spending summary
6. Export CSV
0. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                amount = float(input("Amount: ₹"))
                category = input("Category: ")
                expense_date = ask_date("Date", default_today=True)
                description = input("Description (optional): ")
                expense_id = tracker.add_expense(amount, category, expense_date, description)
                print(f"Added expense #{expense_id}.")
            elif choice == "2":
                category = input("Filter category (leave blank for all): ").strip() or None
                expenses = tracker.list_expenses(category=category)
                if not expenses:
                    print("No expenses found.")
                for item in expenses:
                    print(
                        f"#{item['id']} | ₹{item['amount']:.2f} | {item['category']} | "
                        f"{item['expense_date']} | {item['description']}"
                    )
            elif choice == "3":
                expense_id = int(input("Expense ID to update: "))
                amount = float(input("New amount: ₹"))
                category = input("New category: ")
                expense_date = ask_date("New date", default_today=True)
                description = input("New description (optional): ")
                updated = tracker.update_expense(
                    expense_id,
                    amount=amount,
                    category=category,
                    expense_date=expense_date,
                    description=description,
                )
                print("Expense updated." if updated else "Expense ID not found.")
            elif choice == "4":
                expense_id = int(input("Expense ID to delete: "))
                print("Expense deleted." if tracker.delete_expense(expense_id) else "Expense ID not found.")
            elif choice == "5":
                print(f"Total spending: ₹{tracker.total_spending():.2f}")
                summary = tracker.spending_by_category()
                if summary:
                    print("By category:")
                    for category, total in summary.items():
                        print(f"  {category}: ₹{total:.2f}")
                else:
                    print("No expenses recorded yet.")
            elif choice == "6":
                path = input("CSV output path [expenses.csv]: ").strip() or "expenses.csv"
                count = tracker.export_csv(path)
                print(f"Exported {count} expense(s) to {path}.")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Choose one of the listed options.")
        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
