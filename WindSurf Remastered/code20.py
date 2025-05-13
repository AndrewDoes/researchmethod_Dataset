import random

class MenuItem:
    def __init__(self, name: str, price: float, description: str = ""):
        """
        Initialize a MenuItem.

        Args:
            name (str): Name of the menu item.
            price (float): Price of the menu item.
            description (str, optional): Description of the menu item. Defaults to "".
        """
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> str:
        """
        Get the formatted information of the menu item.

        Returns:
            str: Formatted information of the menu item.
        """
        return f"{self.name} - ${self.price:.2f}: {self.description}"


class Order:
    def __init__(self):
        """
        Initialize an Order.
        """
        self.items = []
        self.total = 0.0
        self.order_id = random.randint(1000, 9999)
        self.payment_method = ""
        self.is_paid = False

    def add_item(self, item: MenuItem) -> None:
        """
        Add a menu item to the order.

        Args:
            item (MenuItem): Menu item to add.
        """
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item: MenuItem) -> None:
        """
        Remove a menu item from the order.

        Args:
            item (MenuItem): Menu item to remove.
        """
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def print_order(self) -> None:
        """
        Print the order details.
        """
        print(f"Order ID: {self.order_id}")
        for item in self.items:
            print(item.get_info())
        print(f"Total: ${self.total:.2f}")
        print("Paid" if self.is_paid else "Not Paid")

    def pay(self, method: str) -> None:
        """
        Pay for the order.

        Args:
            method (str): Payment method.
        """
        self.payment_method = method
        self.is_paid = True
        print(f"Payment successful with {method}.")

    def apply_discount(self) -> None:
        """
        Apply a discount to the order if it has more than 3 items.
        """
        if len(self.items) > 3:
            self.total -= 2
            print("Discount applied.")


class Cafe:
    def __init__(self, name: str):
        """
        Initialize a Cafe.

        Args:
            name (str): Name of the cafe.
        """
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, item: MenuItem) -> None:
        """
        Add a menu item to the cafe's menu.

        Args:
            item (MenuItem): Menu item to add.
        """
        self.menu.append(item)

    def show_menu(self) -> None:
        """
        Print the cafe's menu.
        """
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item.get_info())

    def take_order(self, order: Order) -> None:
        """
        Take an order.

        Args:
            order (Order): Order to take.
        """
        self.orders.append(order)
        print(f"Order {order.order_id} has been placed.")

    def show_orders(self) -> None:
        """
        Print all orders.
        """
        for order in self.orders:
            order.print_order()

    def total_sales(self) -> float:
        """
        Calculate the total sales.

        Returns:
            float: Total sales.
        """
        total = 0.0
        for order in self.orders:
            total += order.total
        return total

    def generate_report(self) -> None:
        """
        Generate a sales report.
        """
        total_sales = self.total_sales()
        print(f"Total sales: ${total_sales:.2f}")
        print(f"Number of orders: {len(self.orders)}")


def main() -> None:
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

   