from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    email: str
    password: str
    age: int
    role: str = field(init=False)

    def __post_init__(self):
        self.role = UserManager.calculate_role(self.age)

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    @staticmethod
    def calculate_role(age: int) -> str:
        if age < 18:
            return "Minor"
        elif 18 <= age <= 60:
            return "Adult"
        else:
            return "Senior"

    def register_user(self):
        print("Register User")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age! Registration failed.")
            return

        user = User(name, email, password, age)
        self.users.append(user)
        print("User Registered!")

    def display_users(self):
        print("\n--- User List ---")
        for u in self.users:
            print(f"Name: {u.name}, Email: {u.email}, Age: {u.age}, Role: {u.role}")

    def update_user(self):
        email = input("Enter email to update: ")
        for u in self.users:
            if u.email == email:
                u.name = input("Enter new name: ")
                u.password = input("Enter new password: ")
                try:
                    u.age = int(input("Enter new age: "))
                except ValueError:
                    print("Invalid age! Update failed.")
                    return
                u.role = self.calculate_role(u.age)
                print("User Updated!")
                return
        print("User not found!")

    def delete_user(self):
        email = input("Enter email to delete: ")
        original_count = len(self.users)
        self.users = [u for u in self.users if u.email != email]
        if len(self.users) < original_count:
            print("User Deleted!")
        else:
            print("User not found!")

    def main_menu(self):
        while True:
            print("\n1. Register User\n2. Display Users\n3. Update User\n4. Delete User\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.display_users()
            elif choice == "3":
                self.update_user()
            elif choice == "4":
                self.delete_user()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

def main():
    manager = UserManager()
    manager.main_menu()

if __name__ == "__main__":
    main()