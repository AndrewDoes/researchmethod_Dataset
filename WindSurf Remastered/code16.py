# Constants
ROLES = {
    "Minor": lambda age: age < 18,
    "Adult": lambda age: 18 <= age <= 60,
    "Senior": lambda age: age > 60
}

# Data Structures
class User:
    def __init__(self, name, email, password, age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.role = self.calculate_role()

    def calculate_role(self):
        for role, condition in ROLES.items():
            if condition(self.age):
                return role
        return "Unknown"

    def update(self, name=None, password=None, age=None):
        if name:
            self.name = name
        if password:
            self.password = password
        if age:
            self.age = age
            self.role = self.calculate_role()

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Role: {self.role}"

# Functions
class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        age = int(input("Enter age: "))
        self.users.append(User(name, email, password, age))
        print("User Registered!")

    def display_users(self):
        print("\n--- User List ---")
        for user in self.users:
            print(user)

    def update_user(self):
        email = input("Enter email to update: ")
        for user in self.users:
            if user.email == email:
                user.update(
                    name=input("Enter new name: "),
                    password=input("Enter new password: "),
                    age=int(input("Enter new age: "))
                )
                print("User Updated!")
                return
        print("User not found!")

    def delete_user(self):
        email = input("Enter email to delete: ")
        self.users = [u for u in self.users if u.email != email]
        print("User Deleted!")

# Main function
def main():
    user_manager = UserManager()
    while True:
        print("\n1. Register User\n2. Display Users\n3. Update User\n4. Delete User\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user_manager.register_user()
        elif choice == "2":
            user_manager.display_users()
        elif choice == "3":
            user_manager.update_user()
        elif choice == "4":
            user_manager.delete_user()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()