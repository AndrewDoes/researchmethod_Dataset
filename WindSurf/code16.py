# WindSurf/code16.py

class User:
    def __init__(self, name, email, password, age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        user = self._get_user_details()
        self.users.append(user)
        print("User Added!")

    def _get_user_details(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        age = int(input("Enter age: "))

        if age < 18:
            print("Age must be 18 or above.")
            return self._get_user_details()

        return User(name, email, password, age)

    def display_users(self):
        if not self.users:
            print("No users available.")
            return

        print("\n--- User List ---")
        for user in self.users:
            print(user)

    def update_user(self):
        name = input("Enter user name to update: ")
        user = self._find_user(name)
        if user:
            user.name = input("Enter new name: ")
            user.email = input("Enter new email: ")
            user.password = input("Enter new password: ")
            user.age = int(input("Enter new age: "))
            print("User Updated!")
        else:
            print("User not found!")

    def _find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def delete_user(self):
        name = input("Enter user name to delete: ")
        self.users = [user for user in self.users if user.name != name]
        print("User Deleted!")

def main():
    user_manager = UserManager()

    while True:
        print("\n1. Register User\n2. Display Users\n3. Update User\n4. Delete User\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            user_manager.add_user()
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
            print("Invalid choice!")

if __name__ == "__main__":
    main()