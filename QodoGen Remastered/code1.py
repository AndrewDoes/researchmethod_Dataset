
"""
Advanced Employee Management System.
"""

from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5  # Fixed number of vacation days that can be paid out.


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            self._payout_holidays()
        else:
            self._take_single_holiday()

    def _payout_holidays(self) -> None:
        """Pay out holidays if enough vacation days are available."""
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"Insufficient holidays for payout. Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out holidays. Holidays left: {self.vacation_days}")

    def _take_single_holiday(self) -> None:
        """Take a single holiday if vacation days are available."""
        if self.vacation_days < 1:
            raise ValueError("No holidays left. Back to work!")
        self.vacation_days -= 1
        print("Enjoy your holiday! Remember to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    """Employee paid based on number of worked hours."""

    hourly_rate: float = 50
    hours_worked: int = 10


@dataclass
class SalariedEmployee(Employee):
    """Employee paid based on a fixed monthly salary."""

    monthly_salary: float = 5000


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the company."""
        self.employees.append(employee)

    def find_employees_by_role(self, role: str) -> List[Employee]:
        """Find employees by role."""
        return [employee for employee in self.employees if employee.role == role]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        if isinstance(employee, SalariedEmployee):
            self._pay_salaried_employee(employee)
        elif isinstance(employee, HourlyEmployee):
            self._pay_hourly_employee(employee)

    def _pay_salaried_employee(self, employee: SalariedEmployee) -> None:
        """Pay a salaried employee."""
        print(f"Paying {employee.name} a monthly salary of ${employee.monthly_salary}.")

    def _pay_hourly_employee(self, employee: HourlyEmployee) -> None:
        """Pay an hourly employee."""
        print(
            f"Paying {employee.name} an hourly rate of ${employee.hourly_rate} for {employee.hours_worked} hours."
        )


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="intern"))

    print(company.find_employees_by_role("vice_president"))
    print(company.find_employees_by_role("manager"))
    print(company.find_employees_by_role("intern"))
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()
