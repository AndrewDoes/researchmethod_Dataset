import json

expenses = []
FILE_NAME = "expenses.json"

def load_expenses():
    global expenses
    try:
        with open(FILE_NAME, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        print("Error loading expenses!")
        expenses = []

def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f)

def add_expense():
    global expenses
    print("\n=== Add Expense ===")
    name = input("Enter expense name: ").strip()
    cost = input("Enter cost: ").strip()
    category = input("Enter category (Food, Travel, Bills): ").strip()
    if not name or not cost.isdigit():
        print("Invalid input!")
        return
    expenses.append({"name": name, "cost": int(cost), "category": category})
    save_expenses()
    print(f"Expense '{name}' added!")

def view_expenses():
    global expenses
    print("\n=== Expense List ===")
    if not expenses:
        print("No expenses recorded.")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ${exp['cost']} - Category: {exp['category']}")

def remove_expense():
    global expenses
    view_expenses()
    try:
        num = int(input("Enter expense number to remove: "))
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            save_expenses()
            print(f"Removed {removed['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

def menu():
    load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Remove Expense\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            remove_expense()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
