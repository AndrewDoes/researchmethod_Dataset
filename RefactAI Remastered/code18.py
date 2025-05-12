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
        print("Customization applied.")

    def get_description(self):
        desc = f"{self.size} {self.name} - ${self.price}"
        if not self.ice:
            desc += " | No Ice"
        if not self.sugar:
            desc += " | No Sugar"
        if self.custom_note != "":
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

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for d in self.drinks:
            print(d.get_description())
        print(f"Total: ${self.total}")
        if self.discount_applied:
            print("Discount applied!")
        print(f"Paid with: {self.payment_method}")

    def pay(self, method):
        self.payment_method = method
        self.loyalty_points += int(self.total // 2)
        print("Payment successful.")

    def cancel_order(self):
        self.drinks.clear()
        self.total = 0.0
        self.discount_applied = False
        self.payment_method = ""
        self.loyalty_points = 0
        print("Order cancelled.")

class Barista:
    def __init__(self, name):
        self.name = name
        self.orders_served = 0
        self.current_order = None

    def take_order(self, order):
        self.current_order = order
        print(f"{self.name} took the order.")

    def serve_order(self):
        if self.current_order:
            self.orders_served += 1
            print("Order served.")
            self.current_order = None

    def report(self):
        print(f"Barista {self.name} served {self.orders_served} orders today.")

# Sample usage
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
