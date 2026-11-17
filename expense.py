# expense-tracker
from datetime import date

expenses = []

print("Daily Expense Tracker")
print("Date:", date.today())
print("Type 'done' when you have finished.\n")

while True:
    amount = input("Expense amount: $")

    if amount.lower() == "done":
        break

    try:
        amount = float(amount)
        description = input("What was it for? ")
        expenses.append((description, amount))
    except ValueError:
        print("Please enter a number, such as 5.50.")

print("\nToday's expenses:")
total = 0

for description, amount in expenses:
    print(f"{description}: ${amount:.2f}")
    total += amount

print(f"\nTotal spent: ${total:.2f}")from datetime import date

expenses = []

print("Daily Expense Tracker")
print("Date:", date.today())
print("Type 'done' when you have finished.\n")

while True:
    amount = input("Expense amount: $")

    if amount.lower() == "done":
        break

    try:
        amount = float(amount)
        description = input("What was it for? ")
        expenses.append((description, amount))
    except ValueError:
        print("Please enter a number, such as 5.50.")

print("\nToday's expenses:")
total = 0

for description, amount in expenses:
    print(f"{description}: ${amount:.2f}")
    total += amount

print(f"\nTotal spent: ${total:.2f}")
