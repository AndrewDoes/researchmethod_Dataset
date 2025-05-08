# WindSurf/code14.py

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.position}, ${self.salary:.2f}"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        """Add employee to company"""
        name = input("Enter employee name: ").strip()
        age = int(input("Enter employee age: ").strip())
        position = input("Enter employee position: ").strip()
        salary = float(input("Enter employee salary: ").strip())
        self.employees.append(Employee(name, age, position, salary))
        print(f"Added '{name}' to company.")

    def view_employees(self):
        """View employees in company"""
        if not self.employees:
            print("No employees available.")
            return
        print("\n=== Company ===")
        for i, employee in enumerate(self.employees, start=1):
            print(f"{i}. {employee}")

def company_menu():
    """Company menu"""
    company = Company()
    while True:
        print("\n1. Add Employee\n2. View Employees\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            company.add_employee()
        elif choice == "2":
            company.view_employees()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    company_menu()