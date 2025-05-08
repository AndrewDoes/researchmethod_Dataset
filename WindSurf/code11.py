# WindSurf/code11.py

import json

# Constants
FILE_NAME = "inventory.json"

# Load inventory from file
def load_inventory():
    """Load inventory from file"""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save inventory to file
def save_inventory(inventory):
    """Save inventory to file"""
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)

# View inventory
def view_inventory(inventory):
    """View inventory"""
    print("\n=== Inventory List ===")
    if not inventory:
        print("No items available.")
        return
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - Qty: {item['quantity']} - ${item['price']} - {item['category']}")

# Add item to inventory
def add_item(inventory):
    """Add item to inventory"""
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    category = input("Enter item category: ")
    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    })
    save_inventory(inventory)
    print(f"Added {name}")

# Remove item from inventory
def remove_item(inventory):
    """Remove item from inventory"""
    view_inventory(inventory)
    try:
        num = int(input("Enter item number to remove: "))
        if 1 <= num <= len(inventory):
            removed = inventory.pop(num - 1)
            save_inventory(inventory)
            print(f"Removed {removed['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

# Main menu
def menu():
    """Main menu"""
    inventory = load_inventory()
    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Remove Item\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            remove_item(inventory)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()