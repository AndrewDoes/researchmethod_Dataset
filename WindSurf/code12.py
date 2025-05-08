items = []
transactions = []

def add_item():
    print("\n=== Add Item ===")
    name = input("Enter item name: ").strip()
    price = input("Enter price: ").strip()
    stock = input("Enter stock: ").strip()
    
    if not price.isdigit() or not stock.isdigit():
        print("❌ Invalid input!")
        return
    
    items.append([name, float(price), int(stock)])
    print(f"✅ Added '{name}' to inventory.")

def view_items():
    if not items:
        print("📭 No items available.")
        return
    
    print("\n=== Inventory ===")
    for i, item in enumerate(items):
        print(f"{i+1}. {item[0]} - ${item[1]:.2f} - Stock: {item[2]}")

def sell_item():
    view_items()
    
    try:
        index = int(input("Enter item number: ")) - 1
        qty = int(input("Enter quantity: "))

        if index < 0 or index >= len(items):
            print("❌ Invalid item number!")
            return

        if items[index][2] < qty:
            print("❌ Not enough stock!")
            return

        total = items[index][1] * qty
        items[index][2] -= qty
        transactions.append([items[index][0], qty, total])
        print(f"🛒 Sold {qty} x {items[index][0]} for ${total:.2f}")

    except ValueError:
        print("❌ Invalid input!")

def view_transactions():
    if not transactions:
        print("📭 No transactions yet.")
        return
    
    print("\n=== Transactions ===")
    for t in transactions:
        print(f"{t[1]} x {t[0]} - ${t[2]:.2f}")

def cashier_menu():
    while True:
        print("\n1. Add Item\n2. View Items\n3. Sell Item\n4. View Transactions\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            sell_item()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    cashier_menu()
