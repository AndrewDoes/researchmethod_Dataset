class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.grades = []
        self.ids = []

    def start(self) -> None:
        """Start the student management system"""
        print("Welcome to the Student Management System!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
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
                print("Invalid choice. Please try again.")

    def display_menu(self) -> None:
        """Display the main menu"""
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grade")
        print("4. Remove Student")
        print("5. Quit")

    def add_student(self) -> None:
        """Add a new student to the system"""
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        if id in self.ids:
            print("Student ID already exists!")
            return
        grade = input("Enter student grade: ")
        self.students.append(name)
        self.ids.append(id)
        self.grades.append(grade)
        print(f"Student {name} (ID: {id}) added with grade {grade}.")

    def view_students(self) -> None:
        """View all students in the system"""
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for i in range(len(self.students)):
            print(f"{self.students[i]} (ID: {self.ids[i]}) - Grade: {self.grades[i]}")

    def update_grade(self) -> None:
        """Update a student's grade"""
        id = input("Enter student ID to update grade: ")
        if id not in self.ids:
            print("Student not found!")
            return
        index = self.ids.index(id)
        new_grade = input("Enter new grade: ")
        self.grades[index] = new_grade
        print(f"Updated grade for {self.students[index]} (ID: {id}) to {new_grade}.")

    def remove_student(self) -> None:
        """Remove a student from the system"""
        id = input("Enter student ID to remove: ")
        if id not in self.ids:
            print("Student not found!")
            return
        index = self.ids.index(id)
        removed_name = self.students.pop(index)
        self.ids.pop(index)
        self.grades.pop(index)
        print(f"Student {removed_name} (ID: {id}) removed.")

def main() -> None:
    system = StudentManagementSystem()
    system.start()

if __name__ == "__main__":
    main()