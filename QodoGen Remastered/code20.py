
import random

class MenuItem:
    def __init__(self, name, price, description=""):
        self.name = name
        self.price = price
        self.description = description

    def get_info(self):
        return f"{self.name} - ${self.price:.2f}: {self.description}"


class Order:
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 2

    def __init__(self):
        self.items = []
        self.total = 0.0
        self.order_id = random.randint(1000, 9999)
        self.payment_method = ""
        self.is_paid = False

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(item.get_info())
        print(f"Total: ${self.total:.2f}")
        print("Paid" if self.is_paid else "Not Paid")

    def pay(self, method):
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self):
        if len(self.items) > self.DISCOUNT_THRESHOLD:
            self.total -= self.DISCOUNT_AMOUNT
            print("Discount applied.")


class Cafe:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item.get_info())

    def take_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self):
        for order in self.orders:
            order.print_order()

    def total_sales(self):
        return sum(order.total for order in self.orders)

    def generate_report(self):
        total_sales = self.total_sales()
        print(f"Total sales: ${total_sales:.2f}")
        print(f"Number of orders: {len(self.orders)}")


def main():
    cafe = Cafe("The Cozy Cafe")

    # Menu items
    menu_items = [
        MenuItem("Coffee", 2.5, "Hot brewed coffee"),
        MenuItem("Tea", 2.0, "Green or black tea"),
        MenuItem("Sandwich", 5.0, "Freshly made sandwich"),
        MenuItem("Cake", 3.0, "Chocolate cake")
    ]

    # Add menu items
    for item in menu_items:
        cafe.add_menu_item(item)

    # Show menu
    cafe.show_menu()

    # Orders
    orders = [
        Order(),
        Order()
    ]

    orders[0].add_item(menu_items[0])
    orders[0].add_item(menu_items[2])
    orders[1].add_item(menu_items[1])
    orders[1].add_item(menu_items[3])

    # Take orders
    for order in orders:
        cafe.take_order(order)

    # Print orders
    for order in orders:
        order.print_order()

    # Apply discount to order 1
    orders[0].apply_discount()

    # Process payments
    orders[0].pay("Credit Card")
    orders[1].pay("Cash")

    # Show cafe orders and sales report
    cafe.show_orders()
    cafe.generate_report()


if __name__ == "__main__":
    main()
