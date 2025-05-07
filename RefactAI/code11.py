import json

FILE_NAME = "inventory.json"
CATEGORIES = ("Electronics", "Clothing", "Food")

class InventoryManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.inventory = []
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.file_name, "r") as f:
                self.inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.inventory = []

    def save_inventory(self):
        with open(self.file_name, "w") as f:
            json.dump(self.inventory, f)

    def add_item(self, name, quantity, price, category):
        self.inventory.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category
        })
        self.save_inventory()

    def remove_item(self, index):
        if 0 <= index < len(self.inventory):
            removed = self.inventory.pop(index)
            self.save_inventory()
            return removed
        return None

    def get_inventory(self):
        return self.inventory

def get_valid_input(prompt, validate_fn, error_msg):
    while True:
        value = input(prompt).strip()
        if validate_fn(value):
            return value
        print(error_msg)

def input_item_details():
    name = get_valid_input("Enter item name: ", lambda x: bool(x), "Name cannot be empty!")
    quantity = int(get_valid_input("Enter quantity: ", lambda x: x.isdigit(), "Quantity must be a positive integer!"))
    price = float(get_valid_input("Enter price: ", lambda x: x.replace('.', '', 1).isdigit(), "Price must be a number!"))
    category = get_valid_input(
        f"Enter category {CATEGORIES}: ",
        lambda x: x in CATEGORIES,
        f"Category must be one of {CATEGORIES}!"
    )
    return name, quantity, price, category

def print_inventory(inventory):
    print("\n=== Inventory List ===")
    if not inventory:
        print("No items available.")
        return
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - Qty: {item['quantity']} - ${item['price']} - {item['category']}")

def main_menu():
    manager = InventoryManager()
    actions = {
        "1": "Add Item",
        "2": "View Inventory",
        "3": "Remove Item",
        "4": "Exit"
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v}" for k, v in actions.items()]))
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\n=== Add Item ===")
            name, quantity, price, category = input_item_details()
            manager.add_item(name, quantity, price, category)
            print(f"Item '{name}' added!")
        elif choice == "2":
            print_inventory(manager.get_inventory())
        elif choice == "3":
            print_inventory(manager.get_inventory())
            if manager.get_inventory():
                idx = get_valid_input(
                    "Enter item number to remove: ",
                    lambda x: x.isdigit() and 1 <= int(x) <= len(manager.get_inventory()),
                    "Invalid item number!"
                )
                removed = manager.remove_item(int(idx) - 1)
                if removed:
                    print(f"Removed {removed['name']}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()