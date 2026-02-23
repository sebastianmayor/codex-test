amount = input("Enter expense amount: ")
description = input("Enter short description: ")

with open("expenses.txt", "a") as file:
    file.write(f"{amount} - {description}\n")

print("Expense saved.")
