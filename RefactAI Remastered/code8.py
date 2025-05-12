from dataclasses import dataclass

@dataclass
class Student:
    name: str
    student_id: str
    grade: str

class StudentManagementSystem:
    def __init__(self):
        self.students = []

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

    def add_student(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        if any(s.student_id == student_id for s in self.students):
            print("Student ID already exists!")
            return
        grade = input("Enter student grade: ")
        self.students.append(Student(name, student_id, grade))
        print(f"Student {name} (ID: {student_id}) added with grade {grade}.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for s in self.students:
            print(f"{s.name} (ID: {s.student_id}) - Grade: {s.grade}")

    def update_grade(self):
        student_id = input("Enter student ID to update grade: ")
        for s in self.students:
            if s.student_id == student_id:
                new_grade = input("Enter new grade: ")
                s.grade = new_grade
                print(f"Updated grade for {s.name} (ID: {student_id}) to {new_grade}.")
                return
        print("Student not found!")

    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        for i, s in enumerate(self.students):
            if s.student_id == student_id:
                removed_name = self.students.pop(i).name
                print(f"Student {removed_name} (ID: {student_id}) removed.")
                return
        print("Student not found!")

def main():
    sms = StudentManagementSystem()
    sms.start()

if __name__ == "__main__":
    main()