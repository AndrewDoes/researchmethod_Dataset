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
            print("Invalid input!")
            return

        self.items.append({
            "name": name,
            "price": float(price),
            "stock": int(stock)
        })
        print(f"Added '{name}' to inventory.")

    def view_items(self):
        if not self.items:
            print("No items available.")
            return

        print("\n=== Inventory ===")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['name']} - ${item['price']:.2f} - Stock: {item['stock']}")

    def sell_item(self):
        self.view_items()

        try:
            index = int(input("Enter item number: ")) - 1
            if index < 0 or index >= len(self.items):
                print("Invalid item number!")
                return

            qty = int(input("Enter quantity: "))
            if self.items[index]["stock"] < qty:
                print("Not enough stock!")
                return

            self.transactions.append({
                "item": self.items[index]["name"],
                "qty": qty,
                "total": self.items[index]["price"] * qty
            })
            self.items[index]["stock"] -= qty
            print(f"Sold {qty} x {self.items[index]['name']}")

        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    manager = InventoryManager()

    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Sell Item")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_item()
        elif choice == "2":
            manager.view_items()
        elif choice == "3":
            manager.sell_item()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()