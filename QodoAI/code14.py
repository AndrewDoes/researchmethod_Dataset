
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.calculate_bonus()

    def calculate_bonus(self):
        position_bonus = {
            "Manager": 5000,
            "Developer": 3000,
            "Intern": 1000
        }
        return position_bonus.get(self.position, 2000)

    def update(self, age, position, salary):
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = self.calculate_bonus()

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Bonus: {self.bonus}"

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("Add Employee")
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")

        self.employees.append(Employee(name, age, position, salary))
        print("Employee Added!")

    def display_employees(self):
        print("\n--- Employee List ---")
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees:
            print(emp)

    def update_employee(self):
        emp_name = input("Enter employee name to update: ")
        for emp in self.employees:
            if emp.name == emp_name:
                age = input("Enter new age: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                emp.update(age, position, salary)
                print("Employee Updated!")
                return
        print("Employee not found!")

    def delete_employee(self):
        emp_name = input("Enter employee name to delete: ")
        self.employees = [emp for emp in self.employees if emp.name != emp_name]
        print("Employee Deleted!")

    def main_menu(self):
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

    def exit_program(self):
        print("Exiting...")
        exit()

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.main_menu()
