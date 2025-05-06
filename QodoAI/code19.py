import random
from typing import List

class Employee:
    def __init__(self, name: str, department: str, salary: float):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = random.randint(1, 10)

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
        self.employees.remove(employee)
        self.total_salary -= employee.salary

    def update_employee_salary(self, employee: Employee, amount: float) -> None:
        employee.update_salary(amount)
        self.total_salary += amount

    def update_employee_performance(self, employee: Employee, score: int) -> None:
        employee.update_performance(score)

    def list_employees(self) -> None:
        for emp in self.employees:
            print(emp.get_info())

    def generate_salary_report(self) -> None:
        print(f"Total salary payout: {self.total_salary}")
        print(f"Total number of employees: {len(self.employees)}")

def main():
    manager = EmployeeManager()

    # Adding employees
    employee1 = Employee("John Doe", "Engineering", 50000)
    employee2 = Employee("Jane Smith", "Marketing", 45000)

    manager.add_employee(employee1)
    manager.add_employee(employee2)

    # Listing employees
    manager.list_employees()

    # Updating employee salary
    manager.update_employee_salary(employee1, 5000)

    # Generating salary report
    manager.generate_salary_report()

if __name__ == "__main__":
    main()