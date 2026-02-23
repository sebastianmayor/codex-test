date = input("Enter expense date (YYYY-MM-DD): ")
amount = input("Enter expense amount: ")
category = input("Enter expense category (e.g., groceries, transport, rent): ")
description = input("Enter short description: ")

with open("expenses.txt", "a") as file:
    file.write(f"{date} | {amount} | {category} | {description}\n")

print("Expense saved.")
