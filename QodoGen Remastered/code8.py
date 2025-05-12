class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    
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
        if student_id in self.students:
            print("Student ID already exists!")
            return
        grade = input("Enter student grade: ")
        self.students[student_id] = {'name': name, 'grade': grade}
        print(f"Student {name} (ID: {student_id}) added with grade {grade}.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for student_id, info in self.students.items():
            print(f"{info['name']} (ID: {student_id}) - Grade: {info['grade']}")

    def update_grade(self):
        student_id = input("Enter student ID to update grade: ")
        if student_id not in self.students:
            print("Student not found!")
            return
        new_grade = input("Enter new grade: ")
        self.students[student_id]['grade'] = new_grade
        print(f"Updated grade for {self.students[student_id]['name']} (ID: {student_id}) to {new_grade}.")

    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        if student_id not in self.students:
            print("Student not found!")
            return
        removed_name = self.students.pop(student_id)['name']
        print(f"Student {removed_name} (ID: {student_id}) removed.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.start()