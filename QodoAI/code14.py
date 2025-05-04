class Employee:
    BONUS_MAP = {
        "Manager": 5000,
        "Developer": 3000,
        "Intern": 1000
    }

    def __init__(self, name: str, age: str, position: str, salary: str) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.BONUS_MAP.get(position, 2000)

    def update(self, age: str, position: str, salary: str) -> None:
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.BONUS_MAP.get(position, 2000)

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Bonus: {self.bonus}"


class EmployeeManagementSystem:
    def __init__(self) -> None:
        self.employees = []

    def add_employee(self) -> None:
        print("Add Employee")
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        self.employees.append(Employee(name, age, position, salary))
        print("Employee Added!")

    def display_employees(self) -> None:
        print("\n--- Employee List ---")
        for emp in self.employees:
            print(emp)

    def update_employee(self) -> None:
        emp_name = input("Enter employee name to update: ")
        employee = self._find_employee(emp_name)
        if employee:
            age = input("Enter new age: ")
            position = input("Enter new position: ")
            salary = input("Enter new salary: ")
            employee.update(age, position, salary)
            print("Employee Updated!")
        else:
            print("Employee not found!")

    def delete_employee(self) -> None:
        emp_name = input("Enter employee name to delete: ")
        self.employees = [emp for emp in self.employees if emp.name != emp_name]
        print("Employee Deleted!")

    def _find_employee(self, name: str) -> Employee:
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def menu(self) -> None:
        actions = {
            "1": self.add_employee,
            "2": self.display_employees,
            "3": self.update_employee,
            "4": self.delete_employee,
            "5": self.exit_program
        }
        while True:
            print("\n1. Add Employee\n2. Display Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
            choice = input("Enter choice: ")
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, try again.")

    def exit_program(self) -> None:
        print("Exiting...")
        exit()


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.menu()