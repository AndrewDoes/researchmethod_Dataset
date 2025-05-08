# WindSurf/code19.py

import random
from typing import List

class Employee:
    def __init__(self, name: str, department: str, salary: float):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = self._generate_performance_score()

    def _generate_performance_score(self) -> int:
        return random.randint(1, 10)

    def get_info(self) -> str:
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}, Performance Score: {self.performance_score}"

    def update_salary(self, amount: float) -> None:
        self.salary += amount
        print(f"Salary of {self.name} updated to {self.salary}")

    def update_performance(self, score: int) -> None:
        self.performance_score = score
        print(f"Performance score of {self.name} updated to {self.performance_score}")

class EmployeeManager:
    def __init__(self):
        self.employees: List[Employee] = []
        self.total_salary = 0.0

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        self.total_salary += employee.salary

    def remove_employee(self, employee: Employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)
            self.total_salary -= employee.salary
        else:
            print("Employee not found")

    def update_employee_salary(self, employee: Employee, amount: float) -> None:
        if employee in self.employees:
            employee.update_salary(amount)
            self.total_salary += amount
        else:
            print("Employee not found")

    def display_employees(self) -> None:
        for employee in self.employees:
            print(employee.get_info())

def main():
    employee_manager = EmployeeManager()

    while True:
        print("\n1. Add Employee\n2. Remove Employee\n3. Update Employee Salary\n4. Display Employees\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, department, salary)
            employee_manager.add_employee(employee)
        elif choice == "2":
            name = input("Enter employee name to remove: ")
            for employee in employee_manager.employees:
                if employee.name == name:
                    employee_manager.remove_employee(employee)
                    break
            else:
                print("Employee not found")
        elif choice == "3":
            name = input("Enter employee name to update salary: ")
            for employee in employee_manager.employees:
                if employee.name == name:
                    amount = float(input("Enter salary update amount: "))
                    employee_manager.update_employee_salary(employee, amount)
                    break
            else:
                print("Employee not found")
        elif choice == "4":
            employee_manager.display_employees()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()