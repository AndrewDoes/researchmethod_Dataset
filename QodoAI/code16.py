class User:
    def __init__(self, name: str, email: str, password: str, age: int) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.role = self._assign_role()

    def _assign_role(self) -> str:
        if self.age < 18:
            return "Minor"
        elif self.age <= 60:
            return "Adult"
        else:
            return "Senior"

    def update(self, name: str, password: str, age: int) -> None:
        self.name = name
        self.password = password
        self.age = age
        self.role = self._assign_role()

    def __str__(self) -> str:
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Role: {self.role}"


class UserManagementSystem:
    def __init__(self) -> None:
        self.users = []

    def register_user(self) -> None:
        print("Register User")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        age = int(input("Enter age: "))
        self.users.append(User(name, email, password, age))
        print("User Registered!")

    def display_users(self) -> None:
        print("\n--- User List ---")
        for user in self.users:
            print(user)

    def update_user(self) -> None:
        email = input("Enter email to update: ")
        user = self._find_user(email)
        if user:
            name = input("Enter new name: ")
            password = input("Enter new password: ")
            age = int(input("Enter new age: "))
            user.update(name, password, age)
            print("User Updated!")
        else:
            print("User not found!")

    def delete_user(self) -> None:
        email = input("Enter email to delete: ")
        self.users = [user for user in self.users if user.email != email]
        print("User Deleted!")

    def _find_user(self, email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def menu(self) -> None:
        actions = {
            "1": self.register_user,
            "2": self.display_users,
            "3": self.update_user,
            "4": self.delete_user,
            "5": self.exit_program
        }
        while True:
            print("\n1. Register User\n2. Display Users\n3. Update User\n4. Delete User\n5. Exit")
            choice = input("Enter choice: ")
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, try again.")

    def exit_program(self) -> None:
        print("Exiting...")
        exit()


if __name__ == "__main__":
    system = UserManagementSystem()
    system.menu()