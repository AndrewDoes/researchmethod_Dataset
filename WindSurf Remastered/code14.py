# WindSurf Remastered/code14.py

class Employee:
    def __init__(self, name, age, position, salary, bonus):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.bonus = bonus

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Bonus: {self.bonus}"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")

        bonus = self.calculate_bonus(position)
        employee = Employee(name, age, position, salary, bonus)
        self.employees.append(employee)
        print("Employee Added!")

    def display_employees(self):
        if not self.employees:
            print("No employees available.")
            return

        print("\n--- Employee List ---")
        for employee in self.employees:
            print(employee)

    def update_employee(self):
        name = input("Enter employee name to update: ")
        for employee in self.employees:
            if employee.name == name:
                employee.age = input("Enter new age: ")
                employee.position = input("Enter new position: ")
                employee.salary = input("Enter new salary: ")
                employee.bonus = self.calculate_bonus(employee.position)
                print("Employee updated!")
                return
        print("Employee not found!")

    def delete_employee(self):
        name = input("Enter employee name to delete: ")
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("Employee deleted!")
                return
        print("Employee not found!")

    def calculate_bonus(self, position):
        bonus_map = {
            "Manager": 5000,
            "Developer": 3000,
            "Intern": 1000
        }
        return bonus_map.get(position, 2000)

    def main_menu(self):
        while True:
            print("\n1. Add Employee\n2. Display Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.display_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    employee_manager = EmployeeManager()
    employee_manager.main_menu()