EXPENSES_FILE = "expenses.txt"


def add_expense():
    date = input("Enter expense date (YYYY-MM-DD): ")
    amount = input("Enter expense amount: ")
    category = input("Enter expense category (e.g., groceries, transport, rent): ")
    description = input("Enter short description: ")

    with open(EXPENSES_FILE, "a") as file:
        file.write(f"{date} | {amount} | {category} | {description}\n")

    print("Expense saved.")


def show_total_expenses():
    total = 0.0

    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")

                if len(parts) < 2:
                    continue

                amount_text = parts[1]

                try:
                    amount = float(amount_text)
                except ValueError:
                    continue

                total += amount
    except FileNotFoundError:
        total = 0.0

    print(f"Total expenses: {total}")


def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1) Add expense")
        print("2) Show total expenses")
        print("3) Quit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
