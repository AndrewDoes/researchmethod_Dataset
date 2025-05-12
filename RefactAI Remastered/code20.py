import random
from typing import List

class MenuItem:
    """Represents a menu item in the cafe."""
    def __init__(self, name: str, price: float, description: str = ""):
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> str:
        """Return a formatted string with menu item details."""
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class Order:
    """Represents a customer's order."""
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 2.0

    def __init__(self):
        self.items: List[MenuItem] = []
        self._total: float = 0.0
        self.order_id: int = random.randint(1000, 9999)
        self.payment_method: str = ""
        self.is_paid: bool = False

    @property
    def total(self) -> float:
        """Return the current total for the order."""
        return self._total

    def add_item(self, item: MenuItem) -> None:
        """Add a menu item to the order and update the total."""
        self.items.append(item)
        self._total += item.price

    def remove_item(self, item: MenuItem) -> None:
        """Remove a menu item from the order and update the total."""
        if item in self.items:
            self.items.remove(item)
            self._total -= item.price

    def print_order(self) -> None:
        """Print the order details."""
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(item.get_info())
        print(f"Total: ${self._total:.2f}")
        print("Paid" if self.is_paid else "Not Paid")

    def pay(self, method: str) -> None:
        """Mark the order as paid and set the payment method."""
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self) -> None:
        """Apply a discount if the order qualifies."""
        if len(self.items) > self.DISCOUNT_THRESHOLD:
            self._total -= self.DISCOUNT_AMOUNT
            print("Discount applied.")

class Cafe:
    """Represents the cafe, its menu, and its orders."""
    def __init__(self, name: str):
        self.name = name
        self.menu: List[MenuItem] = []
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem) -> None:
        """Add a menu item to the cafe's menu."""
        self.menu.append(item)

    def show_menu(self) -> None:
        """Print the cafe's menu."""
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item.get_info())

    def take_order(self, order: Order) -> None:
        """Add an order to the cafe's list of orders."""
        self.orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self) -> None:
        """Print all orders placed at the cafe."""
        for order in self.orders:
            order.print_order()

    @property
    def total_sales(self) -> float:
        """Return the total sales for the cafe."""
        return sum(order.total for order in self.orders)

    def generate_report(self) -> None:
        """Print a sales report for the cafe."""
        print(f"Total sales: ${self.total_sales:.2f}")
        print(f"Number of orders: {len(self.orders)}")

def main():
    cafe = Cafe("The Cozy Cafe")

    # Menu items
    coffee = MenuItem("Coffee", 2.5, "Hot brewed coffee")
    tea = MenuItem("Tea", 2.0, "Green or black tea")
    sandwich = MenuItem("Sandwich", 5.0, "Freshly made sandwich")
    cake = MenuItem("Cake", 3.0, "Chocolate cake")

    # Add menu items
    for item in (coffee, tea, sandwich, cake):
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

    # Apply discount to order 1
    order1.apply_discount()

    # Process payments
    order1.pay("Credit Card")
    order2.pay("Cash")

    # Show cafe orders and sales report
    cafe.show_orders()
    cafe.generate_report()

if __name__ == "__main__":
    main()