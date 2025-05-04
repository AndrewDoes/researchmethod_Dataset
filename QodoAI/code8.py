class Student:
    def __init__(self, name: str, student_id: str, grade: str) -> None:
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.student_id}) - Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self) -> None:
        self.students = []

    def start(self) -> None:
        print("Welcome to the Student Management System!")
        actions = {
            "1": self.add_student,
            "2": self.view_students,
            "3": self.update_grade,
            "4": self.remove_student,
        }
        while True:
            print("\n1. Add Student\n2. View Students\n3. Update Grade\n4. Remove Student\n5. Quit")
            choice = input("Enter choice: ")
            if choice in actions:
                actions[choice]()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    def add_student(self) -> None:
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        if self._find_student_index(student_id) is not None:
            print("Student ID already exists!")
            return
        grade = input("Enter student grade: ")
        self.students.append(Student(name, student_id, grade))
        print(f"Student {name} (ID: {student_id}) added with grade {grade}.")

    def view_students(self) -> None:
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for student in self.students:
            print(student)

    def update_grade(self) -> None:
        student_id = input("Enter student ID to update grade: ")
        index = self._find_student_index(student_id)
        if index is None:
            print("Student not found!")
            return
        new_grade = input("Enter new grade: ")
        self.students[index].grade = new_grade
        print(f"Updated grade for {self.students[index].name} (ID: {student_id}) to {new_grade}.")

    def remove_student(self) -> None:
        student_id = input("Enter student ID to remove: ")
        index = self._find_student_index(student_id)
        if index is None:
            print("Student not found!")
            return
        removed_student = self.students.pop(index)
        print(f"Student {removed_student.name} (ID: {student_id}) removed.")

    def _find_student_index(self, student_id: str) -> int:
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                return index
        return None


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.start()