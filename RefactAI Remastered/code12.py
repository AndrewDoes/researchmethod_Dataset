from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    name: str
    price: float
    stock: int

@dataclass
class Transaction:
    item_name: str
    quantity: int
    total: float

class CashierSystem:
    def __init__(self):
        self.items: List[Item] = []
        self.transactions: List[Transaction] = []

    def add_item(self):
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        price = input("Enter price: ").strip()
        stock = input("Enter stock: ").strip()

        if not self.is_float(price) or not stock.isdigit():
            print("❌ Invalid input!")
            return

        self.items.append(Item(name, float(price), int(stock)))
        print(f"✅ Added '{name}' to inventory.")

    def view_items(self):
        if not self.items:
            print("📭 No items available.")
            return

        print("\n=== Inventory ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f} - Stock: {item.stock}")

    def sell_item(self):
        self.view_items()
        if not self.items:
            return

        try:
            index = int(input("Enter item number: ")) - 1
            qty = int(input("Enter quantity: "))

            if index < 0 or index >= len(self.items):
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

        except ValueError:
            print("❌ Invalid input!")

    def view_transactions(self):
        if not self.transactions:
            print("📭 No transactions yet.")
            return

        print("\n=== Transactions ===")
        for t in self.transactions:
            print(f"{t.quantity} x {t.item_name} - ${t.total:.2f}")

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

    @staticmethod
    def is_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

def main():
    system = CashierSystem()
    system.cashier_menu()

if __name__ == "__main__":
    main()