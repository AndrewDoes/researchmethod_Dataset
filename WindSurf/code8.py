# WindSurf/code8.py

class Student:
    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.grades = []
        self.student_ids = []

    def add_student(self):
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        student_id = input("Enter student ID: ")
        student = Student(name, grade, student_id)
        self.students.append(student)
        self.grades.append(grade)
        self.student_ids.append(student_id)
        print(f"Student '{name}' added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student.name} - Grade: {student.grade} - ID: {student.student_id}")

    def update_grade(self):
        if not self.students:
            print("No students to update.")
            return
        self.view_students()
        try:
            student_num = int(input("Enter student number to update grade: ")) - 1
            if 0 <= student_num < len(self.students):
                new_grade = input("Enter new grade: ")
                self.students[student_num].grade = new_grade
                self.grades[student_num] = new_grade
                print(f"Grade updated for student '{self.students[student_num].name}'.")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Please enter a valid number.")

    def remove_student(self):
        if not self.students:
            print("No students to remove.")
            return
        self.view_students()
        try:
            student_num = int(input("Enter student number to remove: ")) - 1
            if 0 <= student_num < len(self.students):
                removed_student = self.students.pop(student_num)
                self.grades.pop(student_num)
                self.student_ids.pop(student_num)
                print(f"Student '{removed_student.name}' removed successfully.")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Please enter a valid number.")

def start():
    student_management_system = StudentManagementSystem()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Update Grade\n4. Remove Student\n5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            student_management_system.add_student()
        elif choice == "2":
            student_management_system.view_students()
        elif choice == "3":
            student_management_system.update_grade()
        elif choice == "4":
            student_management_system.remove_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    start()