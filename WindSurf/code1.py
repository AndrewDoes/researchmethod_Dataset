"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    def has_enough_vacation_days(self, days: int) -> bool:
        """Check if the employee has enough vacation days."""
        return self.vacation_days >= days

    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday."""
        if not self.has_enough_vacation_days(1):
            raise ValueError("You don't have any holidays left. Now back to work, you!")
        self.vacation_days -= 1

    def payout_holidays(self) -> None:
        """Pay out 5 holidays."""
        if not self.has_enough_vacation_days(FIXED_VACATION_DAYS_PAYOUT):
            raise ValueError(
                f"You don't have enough holidays left over for a payout. Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    amount: int = 10

    def calculate_pay(self) -> float:
        """Calculate the hourly employee's pay."""
        return self.hourly_rate * self.amount


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def calculate_pay(self) -> float:
        """Calculate the salaried employee's pay."""
        return self.monthly_salary


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees_by_role(self, role: str) -> List[Employee]:
        """Find all employees with a specific role."""
        return [employee for employee in self.employees if employee.role == role]

    def pay_employees(self) -> None:
        """Pay all employees."""
        for employee in self.employees:
            if isinstance(employee, SalariedEmployee):
                print(
                    f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
                )
            elif isinstance(employee, HourlyEmployee):
                print(
                    f"Paying employee {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours."
                )


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="intern"))

    managers = company.find_employees_by_role("manager")
    presidents = company.find_employees_by_role("president")
    interns = company.find_employees_by_role("intern")

    print("Managers:", managers)
    print("Presidents:", presidents)
    print("Interns:", interns)

    company.pay_employees()

    employee = company.employees[0]
    employee.take_a_holiday()


if __name__ == "__main__":
    main()