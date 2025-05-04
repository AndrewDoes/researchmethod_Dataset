import random
from typing import List

class Employee:
    def __init__(self, name: str, department: str, salary: float) -> None:
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = self._generate_performance_score()

    def _generate_performance_score(self) -> int:
        return random.randint(1, 10)

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
    def __init__(self) -> None:
        self.employees: List[Employee] = []
        self.total_salary = 0.0

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        self._update_total_salary(employee.salary)

    def remove_employee(self, employee: Employee) -> None:
        self.employees.remove(employee)
        self._update_total_salary(-employee.salary)

    def update_employee_salary(self, employee: Employee, amount: float) -> None:
        employee.update_salary(amount)
        self._update_total_salary(amount)

    def update_employee_performance(self, employee: Employee, score: int) -> None:
        employee.update_performance(score)

    def list_employees(self) -> None:
        for emp in self.employees:
            print(emp.get_info())

    def generate_salary_report(self) -> None:
        print(f"Total salary payout: {self.total_salary}")
        print(f"Total number of employees: {len(self.employees)}")

    def _update_total_salary(self, amount: float) -> None:
        self.total_salary += amount


def main() -> None:
    manager = EmployeeManager()

    # Adding employees
    employees = [
        Employee("John Doe", "Engineering", 50000),
        Employee("Jane Smith", "Marketing", 45000)
    ]

    for employee in employees:
        manager.add_employee(employee)

    # Listing employees
    manager.list_employees()

    # Updating employee salary
    manager.update_employee_salary(employees[0], 5000)

    # Generating salary report
    manager.generate_salary_report()


if __name__ == "__main__":
    main()