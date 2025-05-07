from collections import namedtuple

Item = namedtuple('Item', ['name', 'price', 'stock'])
Transaction = namedtuple('Transaction', ['item_name', 'quantity', 'total'])

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, stock):
        self.items.append(Item(name, price, stock))

    def update_stock(self, index, quantity):
        item = self.items[index]
        self.items[index] = item._replace(stock=item.stock - quantity)

    def get_item(self, index):
        return self.items[index]

    def list_items(self):
        return self.items

    def has_items(self):
        return bool(self.items)

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, item_name, quantity, total):
        self.transactions.append(Transaction(item_name, quantity, total))

    def list_transactions(self):
        return self.transactions

    def has_transactions(self):
        return bool(self.transactions)

def get_valid_input(prompt, validate_fn, error_msg):
    while True:
        value = input(prompt).strip()
        if validate_fn(value):
            return value
        print(error_msg)

def add_item_ui(inventory):
    print("\n=== Add Item ===")
    name = get_valid_input("Enter item name: ", lambda x: bool(x), "Name cannot be empty!")
    price = get_valid_input("Enter price: ", lambda x: x.replace('.', '', 1).isdigit(), "Price must be a number!")
    stock = get_valid_input("Enter stock: ", lambda x: x.isdigit(), "Stock must be an integer!")
    inventory.add_item(name, float(price), int(stock))
    print(f"✅ Added '{name}' to inventory.")

def view_items_ui(inventory):
    if not inventory.has_items():
        print("📭 No items available.")
        return
    print("\n=== Inventory ===")
    for i, item in enumerate(inventory.list_items(), 1):
        print(f"{i}. {item.name} - ${item.price:.2f} - Stock: {item.stock}")

def sell_item_ui(inventory, transaction_manager):
    if not inventory.has_items():
        print("📭 No items available.")
        return
    view_items_ui(inventory)
    try:
        index = int(get_valid_input("Enter item number: ", lambda x: x.isdigit(), "Invalid input!")) - 1
        qty = int(get_valid_input("Enter quantity: ", lambda x: x.isdigit(), "Invalid input!"))
        if index < 0 or index >= len(inventory.items):
            print("❌ Invalid item number!")
            return
        item = inventory.get_item(index)
        if item.stock < qty:
            print("❌ Not enough stock!")
            return
        total = item.price * qty
        inventory.update_stock(index, qty)
        transaction_manager.add_transaction(item.name, qty, total)
        print(f"🛒 Sold {qty} x {item.name} for ${total:.2f}")
    except ValueError:
        print("❌ Invalid input!")

def view_transactions_ui(transaction_manager):
    if not transaction_manager.has_transactions():
        print("📭 No transactions yet.")
        return
    print("\n=== Transactions ===")
    for t in transaction_manager.list_transactions():
        print(f"{t.quantity} x {t.item_name} - ${t.total:.2f}")

def cashier_menu():
    inventory = Inventory()
    transaction_manager = TransactionManager()
    menu_options = {
        "1": ("Add Item", lambda: add_item_ui(inventory)),
        "2": ("View Items", lambda: view_items_ui(inventory)),
        "3": ("Sell Item", lambda: sell_item_ui(inventory, transaction_manager)),
        "4": ("View Transactions", lambda: view_transactions_ui(transaction_manager)),
        "5": ("Exit", None)
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v[0]}" for k, v in menu_options.items()]))
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("👋 Exiting...")
            break
        action = menu_options.get(choice)
        if action:
            action[1]()
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    cashier_menu()