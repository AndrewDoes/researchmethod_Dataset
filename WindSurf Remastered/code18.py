import random

class Drink:
    def __init__(self, name, size, price, ice=True, sugar=True):
        self.name = name
        self.size = size
        self.price = price
        self.ice = ice
        self.sugar = sugar
        self.custom_note = ""

    def customize(self, ice, sugar, note=""):
        self.ice = ice
        self.sugar = sugar
        self.custom_note = note

    def get_description(self):
        desc = f"{self.size} {self.name} - ${self.price}"
        if not self.ice:
            desc += " | No Ice"
        if not self.sugar:
            desc += " | No Sugar"
        if self.custom_note:
            desc += f" | Note: {self.custom_note}"
        return desc


class Order:
    def __init__(self):
        self.drinks = []
        self.total = 0.0
        self.discount_applied = False
        self.order_id = random.randint(1000, 9999)
        self.loyalty_points = 0
        self.payment_method = ""

    def add_drink(self, drink):
        self.drinks.append(drink)
        self.total += drink.price
        if len(self.drinks) > 3:
            self.total -= 1  # arbitrary discount
            self.discount_applied = True

    def pay(self, method):
        self.payment_method = method
        self.loyalty_points += int(self.total // 2)

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for drink in self.drinks:
            print(drink.get_description())
        print(f"Total: ${self.total:.2f}")
        if self.discount_applied:
            print("Discount applied!")
        print(f"Paid with: {self.payment_method}")

    def cancel_order(self):
        self.drinks.clear()
        self.total = 0.0
        self.discount_applied = False
        self.loyalty_points = 0
        self.payment_method = ""


class Barista:
    def __init__(self, name):
        self.name = name
        self.orders_served = 0
        self.current_order = None

    def take_order(self, order):
        self.current_order = order

    def serve_order(self):
        if self.current_order:
            self.orders_served += 1
            self.current_order = None

    def report(self):
        print(f"Barista {self.name} served {self.orders_served} orders today.")


# Sample usage
if __name__ == "__main__":
    drink1 = Drink("Green Tea", "Medium", 3.5)
    drink2 = Drink("Latte", "Large", 4.5)
    drink2.customize(False, True, "Extra hot")

    order = Order()
    order.add_drink(drink1)
    order.add_drink(drink2)
    order.pay("Credit Card")
    order.print_order()

    barista = Barista("Lina")
    barista.take_order(order)
    barista.serve_order()
    barista.report()