import random

# Constants
class Config:
    DISCOUNT_THRESHOLD = 3  # Number of items required for discount
    DISCOUNT_AMOUNT = 2.0  # Discount amount

class MenuItem:
    def __init__(self, name, price, description):
        self._name = name
        self._price = price
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    def get_info(self):
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class OrderItem:
    def __init__(self, item, quantity=1):
        self.item = item
        self.quantity = quantity

    @property
    def total(self):
        return self.item.price * self.quantity

class Order:
    def __init__(self):
        self._items = []
        self._order_id = random.randint(1000, 9999)
        self._payment_method = ""
        self._is_paid = False

    @property
    def items(self):
        return self._items

    @property
    def order_id(self):
        return self._order_id

    @property
    def payment_method(self):
        return self._payment_method

    @property
    def is_paid(self):
        return self._is_paid

    def add_item(self, item, quantity=1):
        self._items.append(OrderItem(item, quantity))

    def remove_item(self, item):
        self._items = [i for i in self._items if i.item != item]

    def calculate_total(self):
        return sum(item.total for item in self._items)

    def apply_discount(self):
        if len(self._items) >= Config.DISCOUNT_THRESHOLD:
            return Config.DISCOUNT_AMOUNT
        return 0

    def pay(self, method):
        self._payment_method = method
        self._is_paid = True

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for item in self._items:
            print(f"{item.item.name} x{item.quantity} - ${item.total:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        if self.is_paid:
            print("Paid")
        else:
            print("Not Paid")

class PaymentProcessor:
    def process_payment(self, order, method):
        order.pay(method)
        print(f"Payment successful with {method}.")

class DiscountManager:
    def apply_discount(self, order):
        discount = order.apply_discount()
        if discount:
            print(f"Discount applied: -${discount:.2f}")

class Cafe:
    def __init__(self, name):
        self._name = name
        self._menu = []
        self._orders = []

    @property
    def name(self):
        return self._name

    @property
    def menu(self):
        return self._menu

    @property
    def orders(self):
        return self._orders

    def add_menu_item(self, item):
        self._menu.append(item)

    def show_menu(self):
        print(f"Menu for {self.name}:")
        for item in self._menu:
            print(item.get_info())

    def take_order(self, order):
        self._orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self):
        for order in self._orders:
            order.print_order()

    def total_sales(self):
        return sum(order.calculate_total() for order in self._orders)

    def generate_report(self):
        total_sales = self.total_sales()
        print(f"Total sales: ${total_sales:.2f}")
        print(f"Number of orders: {len(self._orders)}")

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