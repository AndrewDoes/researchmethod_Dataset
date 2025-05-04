class InventoryItem:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} - Stock: {self.stock}"

    def update_stock(self, quantity: int) -> None:
        if self.stock < quantity:
            raise ValueError("Not enough stock!")
        self.stock -= quantity


class Transaction:
    def __init__(self, item_name: str, quantity: int, total: float) -> None:
        self.item_name = item_name
        self.quantity = quantity
        self.total = total

    def __str__(self) -> str:
        return f"{self.quantity} x {self.item_name} - ${self.total:.2f}"


class CashierSystem:
    def __init__(self) -> None:
        self.items = []
        self.transactions = []

    def add_item(self) -> None:
        print("\n=== Add Item ===")
        name = input("Enter item name: ").strip()
        price = self._get_valid_float("Enter price: ")
        stock = self._get_valid_int("Enter stock: ")

        self.items.append(InventoryItem(name, price, stock))
        print(f"✅ Added '{name}' to inventory.")

    def view_items(self) -> None:
        if not self.items:
            print("📭 No items available.")
            return

        print("\n=== Inventory ===")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")

    def sell_item(self) -> None:
        self.view_items()
        try:
            index = self._get_valid_int("Enter item number: ") - 1
            qty = self._get_valid_int("Enter quantity: ")

            if index < 0 or index >= len(self.items):
                print("❌ Invalid item number!")
                return

            item = self.items[index]
            item.update_stock(qty)
            total = item.price * qty
            self.transactions.append(Transaction(item.name, qty, total))
            print(f"🛒 Sold {qty} x {item.name} for ${total:.2f}")

        except ValueError as e:
            print(f"❌ {e}")

    def view_transactions(self) -> None:
        if not self.transactions:
            print("📭 No transactions yet.")
            return

        print("\n=== Transactions ===")
        for transaction in self.transactions:
            print(transaction)

    def cashier_menu(self) -> None:
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

    def exit_program(self) -> None:
        print("👋 Exiting...")
        exit()

    @staticmethod
    def _get_valid_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    @staticmethod
    def _get_valid_float(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt).strip())
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    system = CashierSystem()
    system.cashier_menu()