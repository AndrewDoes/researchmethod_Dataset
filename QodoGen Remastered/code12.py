class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Stock: {self.stock}"


class Transaction:
    def __init__(self, item_name, quantity, total):
        self.item_name = item_name
        self.quantity = quantity
        self.total = total

    def __str__(self):
        return f"{self.quantity} x {self.item_name} - ${self.total:.2f}"


class InventoryManager:
    def __init__(self):
        self.items = []
        self.transactions = []

    def add_item(self):
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        price = input("Enter price: ").strip()
        stock = input("Enter stock: ").strip()

        if not price.isdigit() or not stock.isdigit():
            print("❌ Invalid input!")
            return

        self.items.append(Item(name, price, stock))
        print(f"✅ Added '{name}' to inventory.")

    def view_items(self):
        if not self.items:
            print("📭 No items available.")
            return

        print("\n=== Inventory ===")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")

    def sell_item(self):
        self.view_items()

        try:
            index = int(input("Enter item number: ")) - 1
            qty = int(input("Enter quantity: "))

            if index < 0 or index >= len(self.items):
                print("❌ Invalid item number!")
                return

            item = self.items[index]
            if not item.update_stock(qty):
                print("❌ Not enough stock!")
                return

            total = item.price * qty
            self.transactions.append(Transaction(item.name, qty, total))
            print(f"🛒 Sold {qty} x {item.name} for ${total:.2f}")

        except ValueError:
            print("❌ Invalid input!")

    def view_transactions(self):
        if not self.transactions:
            print("📭 No transactions yet.")
            return

        print("\n=== Transactions ===")
        for transaction in self.transactions:
            print(transaction)

    def cashier_menu(self):
        while True:
            print("\n1. Add Item\n2. View Items\n3. Sell Item\n4. View Transactions\n5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_items()
            elif choice == "3":
                self.sell_item()
            elif choice == "4":
                self.view_transactions()
            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice!")


if __name__ == "__main__":
    manager = InventoryManager()
    manager.cashier_menu()