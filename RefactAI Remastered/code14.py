from dataclasses import dataclass, field
from typing import List

@dataclass
class Employee:
    name: str
    age: str
    position: str
    salary: str
    bonus: int = field(init=False)

    def __post_init__(self):
        self.bonus = EmployeeManager.calculate_bonus(self.position)

class EmployeeManager:
    def __init__(self):
        self.employees: List[Employee] = []

    @staticmethod
    def calculate_bonus(position: str) -> int:
        if position == "Manager":
            return 5000
        elif position == "Developer":
            return 3000
        elif position == "Intern":
            return 1000
        else:
            return 2000

    def add_employee(self):
        print("Add Employee")
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        employee = Employee(name, age, position, salary)
        self.employees.append(employee)
        print("Employee Added!")

    def display_employees(self):
        print("\n--- Employee List ---")
        for emp in self.employees:
            print(f"Name: {emp.name}, Age: {emp.age}, Position: {emp.position}, Salary: {emp.salary}, Bonus: {emp.bonus}")

    def update_employee(self):
        emp_name = input("Enter employee name to update: ")
        for emp in self.employees:
            if emp.name == emp_name:
                emp.age = input("Enter new age: ")
                emp.position = input("Enter new position: ")
                emp.salary = input("Enter new salary: ")
                emp.bonus = self.calculate_bonus(emp.position)
                print("Employee Updated!")
                return
        print("Employee not found!")

    def delete_employee(self):
        emp_name = input("Enter employee name to delete: ")
        original_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp.name != emp_name]
        if len(self.employees) < original_count:
            print("Employee Deleted!")
        else:
            print("Employee not found!")

    def main_menu(self):
        while True:
            print("\n1. Add Employee\n2. Display Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.display_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

def main():
    manager = EmployeeManager()
    manager.main_menu()

if __name__ == "__main__":
    main()