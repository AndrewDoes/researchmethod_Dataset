class User:
    def __init__(self, name, email, password, age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.role = self.calculate_role(age)

    @staticmethod
    def calculate_role(age):
        if age < 18:
            return "Minor"
        elif 18 <= age <= 60:
            return "Adult"
        else:
            return "Senior"

    def update(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age
        self.role = self.calculate_role(age)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Role: {self.role}"

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, name, email, password, age):
        self.users.append(User(name, email, password, age))
        print("User Registered!")

    def display_users(self):
        print("\n--- User List ---")
        if not self.users:
            print("No users found.")
        for user in self.users:
            print(user)

    def find_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def update_user(self, email):
        user = self.find_user(email)
        if user:
            name = get_input("Enter new name: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            password = get_input("Enter new password: ", lambda x: bool(x.strip()), "Password cannot be empty!")
            age = int(get_input("Enter new age: ", lambda x: x.isdigit(), "Age must be a number!"))
            user.update(name, password, age)
            print("User Updated!")
        else:
            print("User not found!")

    def delete_user(self, email):
        before_count = len(self.users)
        self.users = [user for user in self.users if user.email != email]
        if len(self.users) < before_count:
            print("User Deleted!")
        else:
            print("User not found!")

def get_input(prompt, validate_fn=lambda x: True, error_msg="Invalid input!"):
    while True:
        value = input(prompt)
        if validate_fn(value):
            return value
        print(error_msg)

def main():
    manager = UserManager()
    menu_options = {
        "1": "Register User",
        "2": "Display Users",
        "3": "Update User",
        "4": "Delete User",
        "5": "Exit"
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v}" for k, v in menu_options.items()]))
        choice = input("Enter choice: ")
        if choice == "1":
            print("Register User")
            name = get_input("Enter name: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            email = get_input("Enter email: ", lambda x: bool(x.strip()), "Email cannot be empty!")
            password = get_input("Enter password: ", lambda x: bool(x.strip()), "Password cannot be empty!")
            age = int(get_input("Enter age: ", lambda x: x.isdigit(), "Age must be a number!"))
            manager.register_user(name, email, password, age)
        elif choice == "2":
            manager.display_users()
        elif choice == "3":
            email = get_input("Enter email to update: ", lambda x: bool(x.strip()), "Email cannot be empty!")
            manager.update_user(email)
        elif choice == "4":
            email = get_input("Enter email to delete: ", lambda x: bool(x.strip()), "Email cannot be empty!")
            manager.delete_user(email)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()