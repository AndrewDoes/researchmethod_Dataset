employees = []

def add_employee():
    print("Add Employee")
    name = input("Enter name: ")
    age = input("Enter age: ")
    position = input("Enter position: ")
    salary = input("Enter salary: ")

    if position == "Manager":
        bonus = 5000
    elif position == "Developer":
        bonus = 3000
    elif position == "Intern":
        bonus = 1000
    else:
        bonus = 2000

    employees.append({"name": name, "age": age, "position": position, "salary": salary, "bonus": bonus})
    print("Employee Added!")

def display_employees():
    print("\n--- Employee List ---")
    for emp in employees:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Position: {emp['position']}, Salary: {emp['salary']}, Bonus: {emp['bonus']}")

def update_employee():
    emp_name = input("Enter employee name to update: ")
    for emp in employees:
        if emp['name'] == emp_name:
            emp['age'] = input("Enter new age: ")
            emp['position'] = input("Enter new position: ")
            emp['salary'] = input("Enter new salary: ")

            if emp['position'] == "Manager":
                emp['bonus'] = 5000
            elif emp['position'] == "Developer":
                emp['bonus'] = 3000
            elif emp['position'] == "Intern":
                emp['bonus'] = 1000
            else:
                emp['bonus'] = 2000

            print("Employee Updated!")
            return
    print("Employee not found!")

def delete_employee():
    emp_name = input("Enter employee name to delete: ")
    global employees
    employees = [emp for emp in employees if emp['name'] != emp_name]
    print("Employee Deleted!")

def main():
    while True:
        print("\n1. Add Employee\n2. Display Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

main()
