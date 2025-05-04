"""
Very advanced Employee management system.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Type
from enum import Enum, auto

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class Role(Enum):
    MANAGER = "manager"
    VICE_PRESIDENT = "vice_president"
    INTERN = "intern"
    PRESIDENT = "president"
    OTHER = "other"


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool = False) -> str:
        """
        Let the employee take a single holiday, or pay out 5 holidays.
        Returns a message indicating the result.
        """
        if payout:
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"Not enough holidays left for a payout. Remaining: {self.vacation_days}."
                )
            self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            return f"Paid out {FIXED_VACATION_DAYS_PAYOUT} holidays. Holidays left: {self.vacation_days}"
        else:
            if self.vacation_days < 1:
                raise ValueError("No holidays left. Now back to work, you!")
            self.vacation_days -= 1
            return "Enjoy your holiday. Don't forget to check your emails!"

    def pay(self) -> str:
        """Base pay method, should be overridden by subclasses."""
        return f"Paying employee {self.name}."


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50.0
    hours_worked: int = 10

    def pay(self) -> str:
        total = self.hourly_rate * self.hours_worked
        return (
            f"Paying {self.name} an hourly rate of ${self.hourly_rate} "
            f"for {self.hours_worked} hours. Total: ${total:.2f}"
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000.0

    def pay(self) -> str:
        return f"Paying {self.name} a monthly salary of ${self.monthly_salary:.2f}."


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_by_role(self, role: Role) -> List[Employee]:
        """Find all employees with a specific role."""
        return [emp for emp in self.employees if emp.role == role]

    def pay_employee(self, employee: Employee) -> str:
        """Pay an employee using their own pay logic."""
        return employee.pay()


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_by_role(Role.VICE_PRESIDENT))
    print(company.find_by_role(Role.MANAGER))
    print(company.find_by_role(Role.INTERN))
    print(company.pay_employee(company.employees[0]))
    print(company.employees[0].take_a_holiday(False))


if __name__ == "__main__":
    main()