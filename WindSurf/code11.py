import json

class InventoryManager:
    def __init__(self, file_name):
        self.inventory = []
        self.file_name = file_name

    def load_inventory(self):
        try:
            with open(self.file_name, "r") as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")

    def add_item(self):
        item = input("Enter item: ")
        self.inventory.append(item)
        self.save_inventory()

    def save_inventory(self):
        with open(self.file_name, "w") as f:
            json.dump(self.inventory, f)

    def view_inventory(self):
        if not self.inventory:
            print("No items in inventory.")
            return
        print("\n--- Inventory ---")
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item}")

def main():
    file_name = "inventory.json"
    manager = InventoryManager(file_name)
    manager.load_inventory()

    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_item()
        elif choice == "2":
            manager.view_inventory()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()