# WindSurf/code14.py

# Constants
EMPLOYEE_POSITIONS = ["Manager", "Developer", "Intern"]

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.calculate_bonus()

    def calculate_bonus(self):
        bonuses = {
            "Manager": 5000,
            "Developer": 3000,
            "Intern": 1000
        }
        return bonuses.get(self.position, 2000)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Bonus: {self.bonus}"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        employee = self._get_employee_details()
        self.employees.append(employee)
        print("Employee Added!")

    def _get_employee_details(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        return Employee(name, age, position, salary)

    def display_employees(self):
        if not self.employees:
            print("No employees available.")
            return

        print("\n--- Employee List ---")
        for employee in self.employees:
            print(employee)

    def update_employee(self):
        name = input("Enter employee name to update: ")
        employee = self._find_employee(name)
        if employee:
            employee.age = input("Enter new age: ")
            employee.position = input("Enter new position: ")
            employee.salary = input("Enter new salary: ")
            employee.bonus = employee.calculate_bonus()
            print("Employee Updated!")
        else:
            print("Employee not found!")

    def _find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def delete_employee(self):
        name = input("Enter employee name to delete: ")
        self.employees = [employee for employee in self.employees if employee.name != name]
        print("Employee Deleted!")

def main():
    employee_manager = EmployeeManager()

    while True:
        print("\n1. Add Employee\n2. Display Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            employee_manager.add_employee()
        elif choice == "2":
            employee_manager.display_employees()
        elif choice == "3":
            employee_manager.update_employee()
        elif choice == "4":
            employee_manager.delete_employee()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()