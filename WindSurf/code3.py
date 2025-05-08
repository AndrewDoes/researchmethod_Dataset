class ShoppingCart:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.1
        self.discount_threshold = 100
        self.discount_percentage = 0.05

    def add_item(self, name: str, price: float, quantity: int) -> None:
        """Add an item to the shopping cart"""
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def print_items(self) -> None:
        """Print the items in the shopping cart"""
        print("\n--- Items List ---")
        for item in self.items:
            print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")

    def calculate_total(self) -> float:
        """Calculate the total cost of the items in the shopping cart"""
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def apply_discount(self, total: float) -> float:
        """Apply a discount to the total cost if it exceeds the threshold"""
        if total > self.discount_threshold:
            return total * (1 - self.discount_percentage)
        return total

    def calculate_tax(self, total: float) -> float:
        """Calculate the tax on the total cost"""
        return total * self.tax_rate

    def checkout(self) -> None:
        """Checkout the shopping cart"""
        total = self.calculate_total()
        discounted_total = self.apply_discount(total)
        tax = self.calculate_tax(discounted_total)
        print(f"Subtotal: ${total:.2f}")
        print(f"Discount: ${total - discounted_total:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${discounted_total + tax:.2f}")

def main() -> None:
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart ---")
        print("1. Add item")
        print("2. Print items")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(name, price, quantity)
        elif choice == "2":
            cart.print_items()
        elif choice == "3":
            cart.checkout()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()