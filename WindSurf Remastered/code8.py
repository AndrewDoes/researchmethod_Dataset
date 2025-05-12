# WindSurf Remastered/code8.py

class Student:
    def __init__(self, name, ID, grade):
        self.name = name
        self.ID = ID
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        ID = input("Enter student ID: ")
        if any(student.ID == ID for student in self.students):
            print("Student ID already exists!")
            return
        grade = input("Enter student grade: ")
        self.students.append(Student(name, ID, grade))
        print(f"Student {name} (ID: {ID}) added with grade {grade}.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for student in self.students:
            print(f"{student.name} (ID: {student.ID}) - Grade: {student.grade}")

    def update_grade(self):
        ID = input("Enter student ID to update grade: ")
        student = next((student for student in self.students if student.ID == ID), None)
        if student is None:
            print("Student not found!")
            return
        new_grade = input("Enter new grade: ")
        student.grade = new_grade
        print(f"Updated grade for {student.name} (ID: {ID}) to {new_grade}.")

    def remove_student(self):
        ID = input("Enter student ID to remove: ")
        student = next((student for student in self.students if student.ID == ID), None)
        if student is None:
            print("Student not found!")
            return
        self.students.remove(student)
        print(f"Student {student.name} (ID: {ID}) removed.")

    def start(self):
        print("Welcome to the Student Management System!")
        while True:
            print("\n1. Add Student\n2. View Students\n3. Update Grade\n4. Remove Student\n5. Quit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_grade()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.start()