import random
from typing import List, Optional

class Employee:
    """Represents an employee with name, department, salary, and performance score."""
    def __init__(self, name: str, department: str, salary: float):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = random.randint(1, 10)

    def get_info(self) -> str:
        return (f"Name: {self.name}, Department: {self.department}, "
                f"Salary: {self.salary}, Performance Score: {self.performance_score}")

    def update_salary(self, amount: float) -> None:
        self.salary += amount
        print(f"Salary of {self.name} updated to {self.salary}")

    def update_performance(self, score: int) -> None:
        self.performance_score = score
        print(f"Performance score of {self.name} updated to {self.performance_score}")

class EmployeeManager:
    """Manages a collection of employees and salary operations."""
    def __init__(self):
        self.employees: List[Employee] = []
        self.total_salary: float = 0.0

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        self.total_salary += employee.salary

    def remove_employee_by_name(self, name: str) -> bool:
        employee = self.find_employee_by_name(name)
        if employee:
            self.employees.remove(employee)
            self.total_salary -= employee.salary
            print(f"Employee {name} removed.")
            return True
        print(f"Employee {name} not found.")
        return False

    def find_employee_by_name(self, name: str) -> Optional[Employee]:
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_employee_salary(self, name: str, amount: float) -> None:
        employee = self.find_employee_by_name(name)
        if employee:
            employee.update_salary(amount)
            self.total_salary += amount
        else:
            print(f"Employee {name} not found.")

    def update_employee_performance(self, name: str, score: int) -> None:
        employee = self.find_employee_by_name(name)
        if employee:
            employee.update_performance(score)
        else:
            print(f"Employee {name} not found.")

    def list_employees(self) -> None:
        if not self.employees:
            print("No employees found.")
        for emp in self.employees:
            print(emp.get_info())

    def generate_salary_report(self) -> None:
        print(f"Total salary payout: {self.total_salary}")
        print(f"Total number of employees: {len(self.employees)}")

def main():
    manager = EmployeeManager()

    # Adding employees
    manager.add_employee(Employee("John Doe", "Engineering", 50000))
    manager.add_employee(Employee("Jane Smith", "Marketing", 45000))

    # Listing employees
    manager.list_employees()

    # Updating employee salary
    manager.update_employee_salary("John Doe", 5000)

    # Updating employee performance
    manager.update_employee_performance("Jane Smith", 9)

    # Removing an employee
    manager.remove_employee_by_name("Jane Smith")

    # Generating salary report
    manager.generate_salary_report()

if __name__ == "__main__":
    main()