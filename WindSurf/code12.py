# WindSurf/code12.py

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Stock: {self.stock}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self):
        """Add item to inventory"""
        name = input("Enter item name: ").strip()
        price = self.get_valid_price()
        stock = self.get_valid_stock()
        self.items.append(Item(name, price, stock))
        print(f"Added '{name}' to inventory.")

    def get_valid_price(self):
        """Get valid price from user"""
        while True:
            try:
                price = float(input("Enter price: ").strip())
                if price <= 0:
                    print("Price must be greater than zero.")
                else:
                    return price
            except ValueError:
                print("Invalid price. Please enter a number.")

    def get_valid_stock(self):
        """Get valid stock from user"""
        while True:
            try:
                stock = int(input("Enter stock: ").strip())
                if stock < 0:
                    print("Stock cannot be negative.")
                else:
                    return stock
            except ValueError:
                print("Invalid stock. Please enter a whole number.")

    def view_items(self):
        """View items in inventory"""
        if not self.items:
            print("No items available.")
            return
        print("\n=== Inventory ===")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")

    def sell_item(self):
        """Sell item from inventory"""
        self.view_items()
        try:
            index = int(input("Enter item number: ")) - 1
            if index < 0 or index >= len(self.items):
                print("Invalid item number!")
                return
            qty = int(input("Enter quantity: "))
            if self.items[index].stock < qty:
                print("Not enough stock!")
                return
            # Update stock and print success message
            self.items[index].stock -= qty
            print(f"Sold {qty} {self.items[index].name}(s).")
        except ValueError:
            print("Invalid input!")

def cashier_menu():
    """Cashier menu"""
    inventory = Inventory()
    transactions = []
    while True:
        print("\n1. Add Item\n2. View Items\n3. Sell Item\n4. View Transactions\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            inventory.add_item()
        elif choice == "2":
            inventory.view_items()
        elif choice == "3":
            self = inventory.sell_item()
            transactions.append(self)
        elif choice == "4":
            print("\n=== Transactions ===")
            for transaction in transactions:
                print(transaction)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    cashier_menu()