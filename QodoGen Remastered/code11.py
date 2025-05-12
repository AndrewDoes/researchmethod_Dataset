import json

class InventoryManager:
    FILE_NAME = "inventory.json"

    def __init__(self):
        self.inventory = []
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                self.inventory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.inventory = []

    def save_inventory(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump(self.inventory, f)

    def add_item(self):
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        quantity = input("Enter quantity: ").strip()
        price = input("Enter price: ").strip()
        category = input("Enter category (Electronics, Clothing, Food): ").strip()

        if not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
            print("Invalid input!")
            return

        self.inventory.append({"name": name, "quantity": int(quantity), "price": float(price), "category": category})
        self.save_inventory()
        print(f"Item '{name}' added!")

    def view_inventory(self):
        print("\n=== Inventory List ===")
        if not self.inventory:
            print("No items available.")
            return
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item['name']} - Qty: {item['quantity']} - ${item['price']} - {item['category']}")

    def remove_item(self):
        self.view_inventory()
        try:
            num = int(input("Enter item number to remove: "))
            if 1 <= num <= len(self.inventory):
                removed = self.inventory.pop(num - 1)
                self.save_inventory()
                print(f"Removed {removed['name']}")
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

if __name__ == "__main__":
    manager = InventoryManager()
    manager.menu()