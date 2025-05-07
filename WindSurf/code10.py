# WindSurf/code10.py

import json

class ExpenseManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.file_name, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error loading expenses!")
            return []

    def save_expenses(self):
        with open(self.file_name, "w") as f:
            json.dump(self.expenses, f)

    def add_expense(self):
        expense = input("Enter expense: ")
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense '{expense}' added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses available.")
            return
        print("\n--- Expense List ---")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

    def remove_expense(self):
        if not self.expenses:
            print("No expenses to remove.")
            return
        self.view_expenses()
        try:
            expense_num = int(input("Enter expense number to remove: ")) - 1
            if 0 <= expense_num < len(self.expenses):
                removed_expense = self.expenses.pop(expense_num)
                self.save_expenses()
                print(f"Expense '{removed_expense}' removed successfully.")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Please enter a valid number.")

def menu():
    file_name = "expenses.json"
    expense_manager = ExpenseManager(file_name)
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Remove Expense\n4. Quit")
        choice = input("Enter choice: ")
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
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()