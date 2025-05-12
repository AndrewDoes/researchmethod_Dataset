import random
from typing import List

class Employee:
    """
    Represents an employee with name, department, salary, and performance score.
    """
    def __init__(self, name: str, department: str, salary: float):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = random.randint(1, 10)

    @property
    def info(self) -> str:
        """Return a formatted string with employee details."""
        return (f"Name: {self.name}, Department: {self.department}, "
                f"Salary: {self.salary}, Performance Score: {self.performance_score}")

    def update_salary(self, amount: float) -> None:
        """Update the employee's salary by a given amount."""
        self.salary += amount

    def update_performance(self, score: int) -> None:
        """Set the employee's performance score."""
        self.performance_score = score

class EmployeeManager:
    """
    Manages a collection of Employee objects and salary reporting.
    """
    def __init__(self):
        self.employees: List[Employee] = []
        self.total_salary: float = 0.0

    def add_employee(self, employee: Employee) -> None:
        """Add an employee and update total salary."""
        self.employees.append(employee)
        self.total_salary += employee.salary

    def remove_employee(self, employee: Employee) -> None:
        """Remove an employee and update total salary."""
        if employee in self.employees:
            self.employees.remove(employee)
            self.total_salary -= employee.salary

    def update_employee_salary(self, employee: Employee, amount: float) -> None:
        """Update an employee's salary and adjust total salary."""
        old_salary = employee.salary
        employee.update_salary(amount)
        self.total_salary += (employee.salary - old_salary)

    def update_employee_performance(self, employee: Employee, score: int) -> None:
        """Update an employee's performance score."""
        employee.update_performance(score)

    def list_employees(self) -> List[str]:
        """Return a list of employee info strings."""
        return [emp.info for emp in self.employees]

    def generate_salary_report(self) -> str:
        """Return a formatted salary report."""
        return (f"Total salary payout: {self.total_salary}\n"
                f"Total number of employees: {len(self.employees)}")

def main():
    manager = EmployeeManager()

    # Adding employees
    employee1 = Employee("John Doe", "Engineering", 50000)
    employee2 = Employee("Jane Smith", "Marketing", 45000)

    manager.add_employee(employee1)
    manager.add_employee(employee2)

    # Listing employees
    for info in manager.list_employees():
        print(info)

    # Updating employee salary
    manager.update_employee_salary(employee1, 5000)
    print(f"Salary of {employee1.name} updated to {employee1.salary}")

    # Generating salary report
    print(manager.generate_salary_report())

if __name__ == "__main__":
    main()