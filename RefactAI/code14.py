class Employee:
    BONUS_MAP = {
        "Manager": 5000,
        "Developer": 3000,
        "Intern": 1000
    }
    DEFAULT_BONUS = 2000

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.calculate_bonus(position)

    @classmethod
    def calculate_bonus(cls, position):
        return cls.BONUS_MAP.get(position, cls.DEFAULT_BONUS)

    def update(self, age, position, salary):
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.calculate_bonus(position)

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Position: {self.position}, "
                f"Salary: {self.salary}, Bonus: {self.bonus}")

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, position, salary):
        self.employees.append(Employee(name, age, position, salary))
        print("Employee Added!")

    def display_employees(self):
        print("\n--- Employee List ---")
        if not self.employees:
            print("No employees found.")
        for emp in self.employees:
            print(emp)

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_employee(self, name):
        emp = self.find_employee(name)
        if emp:
            age = input("Enter new age: ")
            position = input("Enter new position: ")
            salary = input("Enter new salary: ")
            emp.update(age, position, salary)
            print("Employee Updated!")
        else:
            print("Employee not found!")

    def delete_employee(self, name):
        before_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp.name != name]
        if len(self.employees) < before_count:
            print("Employee Deleted!")
        else:
            print("Employee not found!")

def get_input(prompt, validate_fn=lambda x: True, error_msg="Invalid input!"):
    while True:
        value = input(prompt)
        if validate_fn(value):
            return value
        print(error_msg)

def main():
    manager = EmployeeManager()
    menu_options = {
        "1": "Add Employee",
        "2": "Display Employees",
        "3": "Update Employee",
        "4": "Delete Employee",
        "5": "Exit"
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v}" for k, v in menu_options.items()]))
        choice = input("Enter choice: ")
        if choice == "1":
            print("Add Employee")
            name = get_input("Enter name: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            age = get_input("Enter age: ", lambda x: x.isdigit(), "Age must be a number!")
            position = get_input("Enter position: ", lambda x: bool(x.strip()), "Position cannot be empty!")
            salary = get_input("Enter salary: ", lambda x: x.replace('.', '', 1).isdigit(), "Salary must be a number!")
            manager.add_employee(name, age, position, salary)
        elif choice == "2":
            manager.display_employees()
        elif choice == "3":
            name = get_input("Enter employee name to update: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            manager.update_employee(name)
        elif choice == "4":
            name = get_input("Enter employee name to delete: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            manager.delete_employee(name)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()