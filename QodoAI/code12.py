
class InventoryItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Stock: {self.stock}"

class Transaction:
    def __init__(self, item_name, quantity, total):
        self.item_name = item_name
        self.quantity = quantity
        self.total = total

    def __str__(self):
        return f"{self.quantity} x {self.item_name} - ${self.total:.2f}"

class CashierSystem:
    def __init__(self):
        self.items = []
        self.transactions = []

    def add_item(self):
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        price = self.get_valid_input("Enter price: ", float)
        stock = self.get_valid_input("Enter stock: ", int)

        self.items.append(InventoryItem(name, price, stock))
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
        index = self.get_valid_input("Enter item number: ", int) - 1
        qty = self.get_valid_input("Enter quantity: ", int)

        if not (0 <= index < len(self.items)):
            print("❌ Invalid item number!")
            return

        item = self.items[index]
        if item.stock < qty:
            print("❌ Not enough stock!")
            return

        total = item.price * qty
        item.stock -= qty
        self.transactions.append(Transaction(item.name, qty, total))
        print(f"🛒 Sold {qty} x {item.name} for ${total:.2f}")

    def view_transactions(self):
        if not self.transactions:
            print("📭 No transactions yet.")
            return

        print("\n=== Transactions ===")
        for transaction in self.transactions:
            print(transaction)

    def cashier_menu(self):
        actions = {
            "1": self.add_item,
            "2": self.view_items,
            "3": self.sell_item,
            "4": self.view_transactions,
            "5": self.exit_program
        }
        while True:
            print("\n1. Add Item\n2. View Items\n3. Sell Item\n4. View Transactions\n5. Exit")
            choice = input("Choose an option: ").strip()
            action = actions.get(choice)
            if action:
                action()
            else:
                print("❌ Invalid choice!")

    def get_valid_input(self, prompt, cast_type):
        while True:
            try:
                return cast_type(input(prompt).strip())
            except ValueError:
                print("❌ Invalid input!")

    def exit_program(self):
        print("👋 Exiting...")
        exit()

if __name__ == "__main__":
    cashier_system = CashierSystem()
    cashier_system.cashier_menu()
