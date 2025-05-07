import random
from typing import List

class MenuItem:
    """Represents a menu item in the cafe."""
    def __init__(self, name: str, price: float, description: str = ""):
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> str:
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class Order:
    """Represents a customer's order."""
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 2.0

    def __init__(self):
        self.items: List[MenuItem] = []
        self.order_id: int = random.randint(1000, 9999)
        self.payment_method: str = ""
        self.is_paid: bool = False
        self._discount_applied: bool = False

    @property
    def total(self) -> float:
        total = sum(item.price for item in self.items)
        if self._discount_applied:
            total -= self.DISCOUNT_AMOUNT
        return max(total, 0.0)

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item: MenuItem):
        if item in self.items:
            self.items.remove(item)

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(item.get_info())
        print(f"Total: ${self.total:.2f}")
        print("Paid" if self.is_paid else "Not Paid")
        if self._discount_applied:
            print("Discount applied.")

    def pay(self, method: str):
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self):
        if len(self.items) > self.DISCOUNT_THRESHOLD:
            self._discount_applied = True
            print("Discount applied.")
        else:
            print("No discount applied (not enough items).")

class Cafe:
    """Represents the cafe, its menu, and orders."""
    def __init__(self, name: str):
        self.name = name
        self.menu: List[MenuItem] = []
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)

    def show_menu(self):
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item.get_info())

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self):
        for order in self.orders:
            order.print_order()

    def total_sales(self) -> float:
        return sum(order.total for order in self.orders)

    def generate_report(self):
        print(f"Total sales: ${self.total_sales():.2f}")
        print(f"Number of orders: {len(self.orders)}")

def main():
    cafe = Cafe("The Cozy Cafe")

    # Menu items
    coffee = MenuItem("Coffee", 2.5, "Hot brewed coffee")
    tea = MenuItem("Tea", 2.0, "Green or black tea")
    sandwich = MenuItem("Sandwich", 5.0, "Freshly made sandwich")
    cake = MenuItem("Cake", 3.0, "Chocolate cake")

    # Add menu items
    for item in [coffee, tea, sandwich, cake]:
        cafe.add_menu_item(item)

    # Show menu
    cafe.show_menu()

    # Order 1
    order1 = Order()
    order1.add_item(coffee)
    order1.add_item(sandwich)

    # Order 2
    order2 = Order()
    order2.add_item(tea)
    order2.add_item(cake)

    # Take orders
    cafe.take_order(order1)
    cafe.take_order(order2)

    # Print orders
    order1.print_order()
    order2.print_order()

    # Apply discount to order 1 (will not apply, only 2 items)
    order1.apply_discount()

    # Add more items to order 1 and apply discount again
    order1.add_item(tea)
    order1.add_item(cake)
    order1.apply_discount()

    # Process payments
    order1.pay("Credit Card")
    order2.pay("Cash")

    # Show cafe orders and sales report
    cafe.show_orders()
    cafe.generate_report()

if __name__ == "__main__":
    main()