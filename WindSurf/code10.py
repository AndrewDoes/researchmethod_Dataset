import json

class ExpenseTracker:
    def __init__(self, file_name):
        self.expenses = []
        self.file_name = file_name

    def load_expenses(self):
        try:
            with open(self.file_name, "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")

    def add_expense(self):
        expense = input("Enter expense: ")
        self.expenses.append(expense)
        self.save_expenses()

    def save_expenses(self):
        with open(self.file_name, "w") as f:
            json.dump(self.expenses, f)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses available.")
            return
        print("\n--- Expense List ---")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

def main():
    file_name = "expenses.json"
    tracker = ExpenseTracker(file_name)
    tracker.load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()