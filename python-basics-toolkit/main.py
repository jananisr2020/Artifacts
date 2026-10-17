"""Interactive command-line entry point."""
from calculator import calculate


def main() -> None:
    print("Python Basics Toolkit")
    print("Operations: +  -  *  /")
    print("Type q at the operation prompt to quit.")

    while True:
        operator = input("\nChoose an operation (+, -, *, /): ").strip()
        if operator.lower() == "q":
            print("Goodbye!")
            break

        if operator not in {"+", "-", "*", "/"}:
            print("Please choose +, -, *, /, or q.")
            continue

        try:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            result = calculate(first, operator, second)
            print(f"Result: {result:g}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
