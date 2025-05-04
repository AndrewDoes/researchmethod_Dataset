
"""
Advanced Employee Management System.
"""

from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed number of vacation days that can be paid out.
DEFAULT_VACATION_DAYS = 25
DEFAULT_HOURLY_RATE = 50
DEFAULT_MONTHLY_SALARY = 5000


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = DEFAULT_VACATION_DAYS

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out holidays."""
        if payout:
            self._payout_holidays()
        else:
            self._take_single_holiday()

    def _payout_holidays(self) -> None:
        """Handle holiday payout for the employee."""
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"Not enough holidays for payout. Remaining: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out holidays. Remaining: {self.vacation_days}")

    def _take_single_holiday(self) -> None:
        """Handle taking a single holiday for the employee."""
        if self.vacation_days < 1:
            raise ValueError("No holidays left. Back to work!")
        self.vacation_days -= 1
        print("Enjoy your holiday. Remember to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    """Employee paid based on the number of worked hours."""

    hourly_rate: float = DEFAULT_HOURLY_RATE
    hours_worked: int = 0

    def calculate_pay(self) -> float:
        """Calculate the pay for the hourly employee."""
        return self.hourly_rate * self.hours_worked


@dataclass
class SalariedEmployee(Employee):
    """Employee paid based on a fixed monthly salary."""

    monthly_salary: float = DEFAULT_MONTHLY_SALARY

    def calculate_pay(self) -> float:
        """Return the monthly salary for the salaried employee."""
        return self.monthly_salary


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the company."""
        self.employees.append(employee)

    def find_employees_by_role(self, role: str) -> List[Employee]:
        """Find all employees with a specific role."""
        return [employee for employee in self.employees if employee.role == role]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee based on their type."""
        pay_amount = employee.calculate_pay()
        print(f"Paying {employee.name} an amount of ${pay_amount}.")


def main() -> None:
    """Main function to demonstrate the Employee Management System."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president", hours_worked=160))
    company.add_employee(HourlyEmployee(name="Tim", role="intern", hours_worked=80))

    for role in ["vice_president", "manager", "intern"]:
        employees = company.find_employees_by_role(role)
        print(f"Employees with role {role}: {employees}")

    for employee in company.employees:
        company.pay_employee(employee)
        employee.take_a_holiday(False)


if __name__ == "__main__":
    main()
