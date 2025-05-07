from typing import List, Tuple

class ShoppingCart:
    def __init__(self, tax_rate: float = 0.1, discount_threshold: float = 100, discount_percent: float = 0.05):
        self.items: List[Tuple[str, float, int]] = []
        self.tax_rate = tax_rate
        self.discount_threshold = discount_threshold
        self.discount_percent = discount_percent

    def add_item(self) -> None:
        """Prompt user to add an item to the cart."""
        name = input("Enter item name: ")
        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            self.items.append((name, price, quantity))
        except ValueError:
            print("Invalid input. Please enter a valid price and quantity.")

    def print_items(self) -> None:
        """Print all items in the cart."""
        print("\n--- Items List ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")

    def calc_total(self) -> float:
        """Calculate the subtotal of all items."""
        return sum(price * quantity for _, price, quantity in self.items)

    def calc_tax(self, subtotal: float) -> float:
        """Calculate the tax for the given subtotal."""
        return subtotal * self.tax_rate

    def apply_discount(self, subtotal: float) -> float:
        """Apply discount if subtotal exceeds the threshold."""
        if subtotal > self.discount_threshold:
            return subtotal * (1 - self.discount_percent)
        return subtotal

    def print_receipt(self) -> None:
        """Print the receipt with all calculations."""
        subtotal = self.calc_total()
        discounted_price = self.apply_discount(subtotal)
        tax = self.calc_tax(discounted_price)
        final_total = discounted_price + tax

        print("\n--- Receipt ---")
        for name, price, quantity in self.items:
            print(f"{name} x{quantity} - ${price * quantity:.2f}")
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${final_total:.2f}")

    def menu(self) -> None:
        """Main menu loop."""
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

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.menu()