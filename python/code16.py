users = []

def register_user():
    print("Register User")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    age = int(input("Enter age: "))

    if age < 18:
        role = "Minor"
    elif age >= 18 and age <= 60:
        role = "Adult"
    else:
        role = "Senior"

    users.append({"name": name, "email": email, "password": password, "age": age, "role": role})
    print("User Registered!")

def display_users():
    print("\n--- User List ---")
    for u in users:
        print(f"Name: {u['name']}, Email: {u['email']}, Age: {u['age']}, Role: {u['role']}")

def update_user():
    email = input("Enter email to update: ")
    for u in users:
        if u['email'] == email:
            u['name'] = input("Enter new name: ")
            u['password'] = input("Enter new password: ")
            u['age'] = int(input("Enter new age: "))

            if u['age'] < 18:
                u['role'] = "Minor"
            elif u['age'] >= 18 and u['age'] <= 60:
                u['role'] = "Adult"
            else:
                u['role'] = "Senior"

            print("User Updated!")
            return
    print("User not found!")

def delete_user():
    email = input("Enter email to delete: ")
    global users
    users = [u for u in users if u['email'] != email]
    print("User Deleted!")

def main():
    while True:
        print("\n1. Register User\n2. Display Users\n3. Update User\n4. Delete User\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

main()
