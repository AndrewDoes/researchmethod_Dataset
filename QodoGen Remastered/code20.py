import random

class MenuItem:
    def __init__(self, n, p, d=""):
        self.name = n
        self.price = p
        self.description = d

    def get_info(self):
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class Order:
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
        if self.is_paid:
            print("Paid")
        else:
            print("Not Paid")

    def pay(self, method):
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self):
        if len(self.items) > 3:
            self.total -= 2
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
        total = 0.0
        for order in self.orders:
            total += order.total
        return total

    def generate_report(self):
        total_sales = self.total_sales()
        print(f"Total sales: ${total_sales:.2f}")
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
