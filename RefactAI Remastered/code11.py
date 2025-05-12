import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Item:
    name: str
    quantity: int
    price: float
    category: str

class InventoryManager:
    FILE_NAME = "inventory.json"
    CATEGORIES = ["Electronics", "Clothing", "Food"]

    def __init__(self):
        self.inventory: List[Item] = []
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
                self.inventory = [Item(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.inventory = []

    def save_inventory(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump([asdict(item) for item in self.inventory], f)

    def add_item(self):
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        quantity = input("Enter quantity: ").strip()
        price = input("Enter price: ").strip()
        category = input(f"Enter category ({', '.join(self.CATEGORIES)}): ").strip()

        if not name or not quantity.isdigit() or not self.is_float(price):
            print("Invalid input!")
            return

        self.inventory.append(Item(name, int(quantity), float(price), category))
        self.save_inventory()
        print(f"Item '{name}' added!")

    def is_float(self, value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    def view_inventory(self):
        print("\n=== Inventory List ===")
        if not self.inventory:
            print("No items available.")
            return
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item.name} - Qty: {item.quantity} - ${item.price} - {item.category}")

    def remove_item(self):
        self.view_inventory()
        if not self.inventory:
            return
        try:
            num = int(input("Enter item number to remove: "))
            if 1 <= num <= len(self.inventory):
                removed = self.inventory.pop(num - 1)
                self.save_inventory()
                print(f"Removed {removed.name}")
            else:
                print("Invalid number!")
        except ValueError:
            print("Invalid input!")

    def menu(self):
        while True:
            print("\n1. Add Item\n2. View Inventory\n3. Remove Item\n4. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_inventory()
            elif choice == "3":
                self.remove_item()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

def main():
    manager = InventoryManager()
    manager.menu()

if __name__ == "__main__":
    main()