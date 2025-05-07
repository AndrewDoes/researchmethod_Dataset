"""
Basic example of a shopping cart system.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    """Class representing an item in the shopping cart."""

    name: str
    price: float
    quantity: int

    @property
    def total_price(self) -> float:
        """Total price of the item."""
        return self.price * self.quantity

class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self) -> None:
        self.items: List[Item] = []
        self.tax_rate = 0.1
        self.discount_threshold = 100
        self.discount_percentage = 0.05

    def add_item(self, name: str, price: float, quantity: int) -> None:
        """Add an item to the shopping cart."""
        self.items.append(Item(name, price, quantity))

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal of the shopping cart."""
        return sum(item.total_price for item in self.items)

    def calculate_tax(self) -> float:
        """Calculate the tax of the shopping cart."""
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate

    def calculate_discount(self) -> float:
        """Calculate the discount of the shopping cart."""
        subtotal = self.calculate_subtotal()
        if subtotal > self.discount_threshold:
            return subtotal * self.discount_percentage
        return 0

    def calculate_total(self) -> float:
        """Calculate the total of the shopping cart."""
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        return subtotal + tax - discount

def main() -> None:
    """Main function."""

    cart = ShoppingCart()

    while True:
        print("1. Add item")
        print("2. View cart")
        print("3. Checkout")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            cart.add_item(name, price, quantity)
        elif choice == "2":
            print("Shopping Cart:")
            for i, item in enumerate(cart.items, start=1):
                print(f"{i}. {item.name} x {item.quantity} = ${item.total_price:.2f}")
            print(f"Subtotal: ${cart.calculate_subtotal():.2f}")
            print(f"Tax: ${cart.calculate_tax():.2f}")
            print(f"Discount: ${cart.calculate_discount():.2f}")
            print(f"Total: ${cart.calculate_total():.2f}")
        elif choice == "3":
            print("Checkout:")
            print(f"Total: ${cart.calculate_total():.2f}")
            print("Thank you for shopping!")
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()