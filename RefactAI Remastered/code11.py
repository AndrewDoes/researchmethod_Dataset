import json

inventory = []
FILE_NAME = "inventory.json"

def load_inventory():
    global inventory
    try:
        with open(FILE_NAME, "r") as f:
            inventory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        inventory = []

def save_inventory():
    with open(FILE_NAME, "w") as f:
        json.dump(inventory, f)

def add_item():
    global inventory
    print("\n=== Add Item ===")
    name = input("Enter item name: ").strip()
    quantity = input("Enter quantity: ").strip()
    price = input("Enter price: ").strip()
    category = input("Enter category (Electronics, Clothing, Food): ").strip()
    
    if not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
        print("Invalid input!")
        return
    
    inventory.append({"name": name, "quantity": int(quantity), "price": float(price), "category": category})
    save_inventory()
    print(f"Item '{name}' added!")

def view_inventory():
    print("\n=== Inventory List ===")
    if not inventory:
        print("No items available.")
        return
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - Qty: {item['quantity']} - ${item['price']} - {item['category']}")

def remove_item():
    global inventory
    view_inventory()
    try:
        num = int(input("Enter item number to remove: "))
        if 1 <= num <= len(inventory):
            removed = inventory.pop(num - 1)
            save_inventory()
            print(f"Removed {removed['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

def menu():
    load_inventory()
    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Remove Item\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
