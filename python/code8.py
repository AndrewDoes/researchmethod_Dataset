students = []
grades = []
IDs = []

def start():
    print("Welcome to the Student Management System!")
    while True:
        print("\n1. Add Student\n2. View Students\n3. Update Grade\n4. Remove Student\n5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

def add_student():
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    if ID in IDs:
        print("Student ID already exists!")
        return
    grade = input("Enter student grade: ")
    students.append(name)
    IDs.append(ID)
    grades.append(grade)
    print(f"Student {name} (ID: {ID}) added with grade {grade}.")

def view_students():
    if len(students) == 0:
        print("No students available.")
        return
    print("\n--- Student List ---")
    for i in range(len(students)):
        print(f"{students[i]} (ID: {IDs[i]}) - Grade: {grades[i]}")

def update_grade():
    ID = input("Enter student ID to update grade: ")
    if ID not in IDs:
        print("Student not found!")
        return
    index = IDs.index(ID)
    new_grade = input("Enter new grade: ")
    grades[index] = new_grade
    print(f"Updated grade for {students[index]} (ID: {ID}) to {new_grade}.")

def remove_student():
    ID = input("Enter student ID to remove: ")
    if ID not in IDs:
        print("Student not found!")
        return
    index = IDs.index(ID)
    removed_name = students.pop(index)
    IDs.pop(index)
    grades.pop(index)
    print(f"Student {removed_name} (ID: {ID}) removed.")

start()
