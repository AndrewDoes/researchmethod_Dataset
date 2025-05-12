
class ShoppingCart:
    def __init__(self, tax_rate=0.1, discount_threshold=100, discount_percentage=0.05):
        self.items = []
        self.tax_rate = tax_rate
        self.discount_threshold = discount_threshold
        self.discount_percentage = discount_percentage

    def add_item(self, name, price, quantity):
        self.items.append((name, float(price), int(quantity)))

    def print_items(self):
        print("\n--- Items List ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")

    def calculate_total(self):
        return sum(price * quantity for _, price, quantity in self.items)

    def calculate_tax(self, total):
        return total * self.tax_rate

    def apply_discount(self, total):
        if total > self.discount_threshold:
            return total * (1 - self.discount_percentage)
        return total

    def print_receipt(self):
        total = self.calculate_total()
        tax = self.calculate_tax(total)
        discounted_price = self.apply_discount(total)
        final_total = discounted_price + tax

        print("\n--- Receipt ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")
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
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
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
