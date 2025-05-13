import json

# Constants
FILE_NAME = "inventory.json"

# Data Structures
class InventoryItem:
    def __init__(self, name, quantity, price, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category
        }

class Inventory:
    def __init__(self):
        self.items = []

    def load(self):
        try:
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                self.items = [InventoryItem(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save(self):
        data = [item.to_dict() for item in self.items]
        with open(FILE_NAME, "w") as f:
            json.dump(data, f)

    def add_item(self, name, quantity, price, category):
        item = InventoryItem(name, quantity, price, category)
        self.items.append(item)
        self.save()

    def view_inventory(self):
        print("\n=== Inventory List ===")
        if not self.items:
            print("No items available.")
            return
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - Qty: {item.quantity} - ${item.price} - {item.category}")

    def remove_item(self, num):
        try:
            num = int(num)
            if 1 <= num <= len(self.items):
                removed = self.items.pop(num - 1)
                self.save()
                print(f"Removed {removed.name}")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input!")

def main_menu():
    inventory = Inventory()
    inventory.load()

    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Remove Item\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            quantity = input("Enter quantity: ").strip()
            price = input("Enter price: ").strip()
            category = input("Enter category (Electronics, Clothing, Food): ").strip()

            if not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
                print("Invalid input!")
                continue

            inventory.add_item(name, int(quantity), float(price), category)
            print(f"Item '{name}' added!")

        elif choice == "2":
            inventory.view_inventory()

        elif choice == "3":
            inventory.view_inventory()
            num = input("Enter item number to remove: ")
            inventory.remove_item(num)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()