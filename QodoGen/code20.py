import random
from typing import List

class MenuItem:
    def __init__(self, name: str, price: float, description: str = ""):
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> str:
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class Order:
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 2

    def __init__(self):
        self.items: List[MenuItem] = []
        self.total = 0.0
        self.order_id = random.randint(1000, 9999)
        self.payment_method = ""
        self.is_paid = False

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item: MenuItem) -> None:
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def print_order(self) -> None:
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(item.get_info())
        print(f"Total: ${self.total:.2f}")
        print("Paid" if self.is_paid else "Not Paid")

    def pay(self, method: str) -> None:
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self) -> None:
        if len(self.items) > self.DISCOUNT_THRESHOLD:
            self.total -= self.DISCOUNT_AMOUNT
            print("Discount applied.")

class Cafe:
    def __init__(self, name: str):
        self.name = name
        self.menu: List[MenuItem] = []
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem) -> None:
        self.menu.append(item)

    def show_menu(self) -> None:
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item.get_info())

    def take_order(self, order: Order) -> None:
        self.orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self) -> None:
        for order in self.orders:
            order.print_order()

    def total_sales(self) -> float:
        return sum(order.total for order in self.orders)

    def generate_report(self) -> None:
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
    cafe.add_menu_item(coffee)
    cafe.add_menu_item(tea)
    cafe.add_menu_item(sandwich)
    cafe.add_menu_item(cake)

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