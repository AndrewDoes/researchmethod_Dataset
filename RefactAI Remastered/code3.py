class ShoppingCart:
    TAX_RATE = 0.1
    DISCOUNT_THRESHOLD = 100
    DISCOUNT_PERCENT = 0.05

    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("Enter item name: ")
        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            self.items.append((name, price, quantity))
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    def print_items(self):
        print("\n--- Items List ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")

    def subtotal(self):
        return sum(price * quantity for _, price, quantity in self.items)

    def tax(self, amount=None):
        if amount is None:
            amount = self.subtotal()
        return amount * self.TAX_RATE

    def discounted_subtotal(self):
        subtotal = self.subtotal()
        if subtotal > self.DISCOUNT_THRESHOLD:
            return subtotal * (1 - self.DISCOUNT_PERCENT)
        return subtotal

    def print_receipt(self):
        subtotal = self.subtotal()
        discounted = self.discounted_subtotal()
        tax = self.tax(discounted)
        total = discounted + tax

        print("\n--- Receipt ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Discounted Price: ${discounted:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

    def menu(self):
        while True:
            print("\n1. Add Item\n2. View Items\n3. Print Receipt\n4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.print_items()
            elif choice == "3":
                self.print_receipt()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


def main():
    cart = ShoppingCart()
    cart.menu()


if __name__ == "__main__":
    main()