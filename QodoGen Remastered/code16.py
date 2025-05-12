class User:
    def __init__(self, name, email, password, age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.role = self.assign_role()

    def assign_role(self):
        if self.age < 18:
            return "Minor"
        elif self.age <= 60:
            return "Adult"
        else:
            return "Senior"

    def update(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age
        self.role = self.assign_role()

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Role: {self.role}"


class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self):
        print("Register User")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        age = int(input("Enter age: "))

        new_user = User(name, email, password, age)
        self.users.append(new_user)
        print("User Registered!")

    def display_users(self):
        print("\n--- User List ---")
        for user in self.users:
            print(user)

    def update_user(self):
        email = input("Enter email to update: ")
        for user in self.users:
            if user.email == email:
                name = input("Enter new name: ")
                password = input("Enter new password: ")
                age = int(input("Enter new age: "))
                user.update(name, password, age)
                print("User Updated!")
                return
        print("User not found!")

    def delete_user(self):
        email = input("Enter email to delete: ")
        self.users = [user for user in self.users if user.email != email]
        print("User Deleted!")

    def menu(self):
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


if __name__ == "__main__":
    manager = UserManager()
    manager.menu()