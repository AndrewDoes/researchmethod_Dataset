from dataclasses import dataclass, field
from typing import List

TAX_RATE = 0.1
DISCOUNT_THRESHOLD = 100
DISCOUNT_PERCENT = 0.05

@dataclass
class Item:
    name: str
    price: float
    quantity: int

    def total(self) -> float:
        return self.price * self.quantity

@dataclass
class Cart:
    items: List[Item] = field(default_factory=list)

    def add_item(self, name: str, price: float, quantity: int) -> None:
        self.items.append(Item(name, price, quantity))

    def subtotal(self) -> float:
        return sum(item.total() for item in self.items)

    def discount(self) -> float:
        subtotal = self.subtotal()
        if subtotal > DISCOUNT_THRESHOLD:
            return subtotal * DISCOUNT_PERCENT
        return 0.0

    def tax(self, after_discount: float) -> float:
        return after_discount * TAX_RATE

    def final_total(self) -> float:
        subtotal = self.subtotal()
        discount = self.discount()
        discounted_price = subtotal - discount
        tax = self.tax(discounted_price)
        return discounted_price + tax

    def print_items(self) -> None:
        print("\n--- Items List ---")
        for item in self.items:
            print(f"{item.name} x{item.quantity} - ${item.total():.2f}")

    def print_receipt(self) -> None:
        subtotal = self.subtotal()
        discount = self.discount()
        discounted_price = subtotal - discount
        tax = self.tax(discounted_price)
        total = discounted_price + tax

        print("\n--- Receipt ---")
        for item in self.items:
            print(f"{item.name} x{item.quantity} - ${item.total():.2f}")
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    cart = Cart()
    while True:
        print("\n1. Add Item\n2. View Items\n3. Print Receipt\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            price = get_float("Enter price: ")
            quantity = get_int("Enter quantity: ")
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