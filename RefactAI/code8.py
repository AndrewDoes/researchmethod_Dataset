from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Student:
    name: str
    student_id: str
    grade: str

class StudentManager:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        if self.find_student(student_id):
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
        for student in self.students:
            print(f"{student.name} (ID: {student.student_id}) - Grade: {student.grade}")

    def update_grade(self):
        student_id = input("Enter student ID to update grade: ")
        student = self.find_student(student_id)
        if not student:
            print("Student not found!")
            return
        new_grade = input("Enter new grade: ")
        student.grade = new_grade
        print(f"Updated grade for {student.name} (ID: {student_id}) to {new_grade}.")

    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        student = self.find_student(student_id)
        if not student:
            print("Student not found!")
            return
        self.students.remove(student)
        print(f"Student {student.name} (ID: {student_id}) removed.")

    def find_student(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

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
    StudentManager().start()