# WindSurf Remastered/code12.py

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Stock: {self.stock}"


class Transaction:
    def __init__(self, item, quantity, total):
        self.item = item
        self.quantity = quantity
        self.total = total

    def __str__(self):
        return f"{self.item.name} x {self.quantity} - ${self.total:.2f}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, stock):
        try:
            item = Item(name, price, stock)
            self.items.append(item)
            print(f"✅ Added '{name}' to inventory.")
        except ValueError:
            print("❌ Invalid input!")

    def view_items(self):
        if not self.items:
            print("📭 No items available.")
            return

        print("\n=== Inventory ===")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")


class Cashier:
    def __init__(self, inventory):
        self.inventory = inventory
        self.transactions = []

    def sell_item(self):
        self.inventory.view_items()

        try:
            index = int(input("Enter item number: ")) - 1
            qty = int(input("Enter quantity: "))

            if index < 0 or index >= len(self.inventory.items):
                print("❌ Invalid item number!")
                return

            item = self.inventory.items[index]
            if item.stock < qty:
                print("❌ Not enough stock!")
                return

            total = item.price * qty
            item.stock -= qty
            transaction = Transaction(item, qty, total)
            self.transactions.append(transaction)
            print(f"🛒 Sold {qty} x {item.name} for ${total:.2f}")
        except ValueError:
            print("❌ Invalid input!")


def cashier_menu():
    inventory = Inventory()
    cashier = Cashier(inventory)

    while True:
        print("\n1. Add Item\n2. View Items\n3. Sell Item\n4. View Transactions\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            price = input("Enter price: ").strip()
            stock = input("Enter stock: ").strip()
            cashier.inventory.add_item(name, price, stock)
        elif choice == "2":
            cashier.inventory.view_items()
        elif choice == "3":
            cashier.sell_item()
        elif choice == "4":
            if not cashier.transactions:
                print("📭 No transactions yet.")
                continue

            print("\n=== Transactions ===")
            for transaction in cashier.transactions:
                print(transaction)
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    cashier_menu()