
import json

FILE_NAME = "inventory.json"

def load_inventory():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(inventory):
    with open(FILE_NAME, "w") as f:
        json.dump(inventory, f)

def get_user_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt).strip()
        if validation_func and not validation_func(user_input):
            print("Invalid input!")
        else:
            return user_input

def is_valid_quantity(quantity):
    return quantity.isdigit()

def is_valid_price(price):
    return price.replace('.', '', 1).isdigit()

def add_item(inventory):
    print("\n=== Add Item ===")
    name = get_user_input("Enter item name: ")
    quantity = get_user_input("Enter quantity: ", is_valid_quantity)
    price = get_user_input("Enter price: ", is_valid_price)
    category = get_user_input("Enter category (Electronics, Clothing, Food): ")

    inventory.append({
        "name": name,
        "quantity": int(quantity),
        "price": float(price),
        "category": category
    })
    save_inventory(inventory)
    print(f"Item '{name}' added!")

def view_inventory(inventory):
    print("\n=== Inventory List ===")
    if not inventory:
        print("No items available.")
        return
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - Qty: {item['quantity']} - ${item['price']} - {item['category']}")

def remove_item(inventory):
    view_inventory(inventory)
    try:
        num = int(get_user_input("Enter item number to remove: "))
        if 1 <= num <= len(inventory):
            removed = inventory.pop(num - 1)
            save_inventory(inventory)
            print(f"Removed {removed['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

def menu():
    inventory = load_inventory()
    actions = {
        "1": lambda: add_item(inventory),
        "2": lambda: view_inventory(inventory),
        "3": lambda: remove_item(inventory),
        "4": lambda: exit_program()
    }
    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Remove Item\n4. Exit")
        choice = get_user_input("Choose an option: ")
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice!")

def exit_program():
    print("Exiting...")
    exit()

if __name__ == "__main__":
    menu()
