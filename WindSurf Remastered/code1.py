# WindSurf Remastered/code1.py

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

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            self._pay_out_holiday()
        else:
            self._take_single_holiday()

    def _pay_out_holiday(self) -> None:
        """Pay out 5 holidays."""
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"You don't have enough holidays left over for a payout. Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    def _take_single_holiday(self) -> None:
        """Take a single holiday."""
        if self.vacation_days < 1:
            raise ValueError("You don't have any holidays left. Now back to work, you!")
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""
    monthly_salary: float = 5000

@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""
    hourly_rate: float = 50
    amount: int = 10

class Company:
    """Represents a company with employees."""
    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees_by_role(self, role: str) -> List[Employee]:
        """Find all employees with the given role."""
        return [employee for employee in self.employees if employee.role == role]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        if isinstance(employee, SalariedEmployee):
            print(f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}.")
        elif isinstance(employee, HourlyEmployee):
            print(f"Paying employee {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours.")

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