
import json

class ExpenseManager:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = []
        self.load_expenses()

    def load_expenses(self) -> None:
        try:
            with open(self.file_name, "r") as f:
                self.expenses = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self) -> None:
        with open(self.file_name, "w") as f:
            json.dump(self.expenses, f)

    def add_expense(self) -> None:
        print("\n=== Add Expense ===")
        name = input("Enter expense name: ").strip()
        cost = input("Enter cost: ").strip()
        category = input("Enter category (Food, Travel, Bills): ").strip()
        if not name or not cost.isdigit():
            print("Invalid input!")
            return
        self.expenses.append({"name": name, "cost": int(cost), "category": category})
        self.save_expenses()
        print(f"Expense '{name}' added!")

    def view_expenses(self) -> None:
        print("\n=== Expense List ===")
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['name']} - ${exp['cost']} - Category: {exp['category']}")

    def remove_expense(self) -> None:
        self.view_expenses()
        try:
            num = int(input("Enter expense number to remove: "))
            if 1 <= num <= len(self.expenses):
                removed = self.expenses.pop(num - 1)
                self.save_expenses()
                print(f"Removed {removed['name']}")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input!")

    def menu(self) -> None:
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
    manager = ExpenseManager()
    manager.menu()
