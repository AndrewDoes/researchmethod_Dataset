import json
from typing import List

class Expense:
    def __init__(self, name: str, cost: int, category: str):
        self.name = name
        self.cost = cost
        self.category = category

    def to_dict(self):
        return {"name": self.name, "cost": self.cost, "category": self.category}

    @staticmethod
    def from_dict(data):
        return Expense(data["name"], data["cost"], data["category"])

    def __str__(self):
        return f"{self.name} - ${self.cost} - Category: {self.category}"

class ExpenseTracker:
    FILE_NAME = "expenses.json"

    def __init__(self):
        self.expenses: List[Expense] = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(exp) for exp in data]
        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            print("Error loading expenses!")
            self.expenses = []

    def save_expenses(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump([exp.to_dict() for exp in self.expenses], f)

    def add_expense(self):
        print("\n=== Add Expense ===")
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
        print("\n=== Expense List ===")
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp}")

    def remove_expense(self):
        self.view_expenses()
        if not self.expenses:
            return
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

    def menu(self):
        while True:
            print("\n1. Add Expense\n2. View Expenses\n3. Remove Expense\n4. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.remove_expense()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    ExpenseTracker().menu()