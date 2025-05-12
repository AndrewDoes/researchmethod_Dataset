import json

# Constants
FILE_NAME = "expenses.json"

# Expense class
class Expense:
    def __init__(self, name, cost, category):
        self.name = name
        self.cost = cost
        self.category = category

# Expense Manager class
class ExpenseManager:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(FILE_NAME, "r") as f:
                return [Expense(**expense) for expense in json.load(f)]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error loading expenses!")
            return []

    def save_expenses(self):
        with open(FILE_NAME, "w") as f:
            json.dump([expense.__dict__ for expense in self.expenses], f)

    def add_expense(self):
        name = input("Enter expense name: ").strip()
        cost = input("Enter cost: ").strip()
        category = input("Enter category (Food, Travel, Bills): ").strip()
        if not name or not cost.isdigit():
            print("Invalid input!")
            return
        self.expenses.append(Expense(name, int(cost), category))
        self.save_expenses()
        print(f"Expense '{name}' added!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense.name} - ${expense.cost} - Category: {expense.category}")

    def remove_expense(self):
        self.view_expenses()
        try:
            num = int(input("Enter expense number to remove: "))
            if 1 <= num <= len(self.expenses):
                removed = self.expenses.pop(num - 1)
                self.save_expenses()
                print(f"Removed {removed.name}")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input!")

# Menu function
def menu():
    expense_manager = ExpenseManager()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Remove Expense\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            expense_manager.add_expense()
        elif choice == "2":
            expense_manager.view_expenses()
        elif choice == "3":
            expense_manager.remove_expense()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()