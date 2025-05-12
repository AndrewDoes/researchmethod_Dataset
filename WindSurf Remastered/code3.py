# WindSurf Remastered/code3.py

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.1
        self.discount_threshold = 100
        self.discount_percentage = 0.05

    def add_item(self, name, price, quantity):
        """Add an item to the shopping cart"""
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_total(self):
        """Calculate the total cost of all items in the cart"""
        return sum(item["price"] * item["quantity"] for item in self.items)

    def calculate_tax(self):
        """Calculate the tax on the total cost"""
        return self.calculate_total() * self.tax_rate

    def apply_discount(self):
        """Apply a discount if the total cost exceeds the threshold"""
        total = self.calculate_total()
        if total > self.discount_threshold:
            return total * (1 - self.discount_percentage)
        return total

    def print_items(self):
        """Print a list of all items in the cart"""
        print("\n--- Items List ---")
        for item in self.items:
            print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")

    def print_receipt(self):
        """Print a receipt with the total cost, tax, and discount"""
        total = self.calculate_total()
        tax = self.calculate_tax()
        discounted_price = self.apply_discount()
        final_total = discounted_price + tax

        print("\n--- Receipt ---")
        for item in self.items:
            print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")
        print(f"\nSubtotal: ${total:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${final_total:.2f}")


def main():
    cart = ShoppingCart()

    while True:
        print("\n1. Add Item\n2. View Items\n3. Print Receipt\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(name, price, quantity)
        elif choice == "2":
            cart.print_items()
        elif choice == "3":
            cart.print_receipt()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()