import random
from typing import List, Optional

class Drink:
    def __init__(self, name: str, size: str, price: float, ice: bool = True, sugar: bool = True):
        self.name = name
        self.size = size
        self.price = price
        self.ice = ice
        self.sugar = sugar
        self.custom_note = ""

    def customize(self, ice: bool, sugar: bool, note: str = ""):
        self.ice = ice
        self.sugar = sugar
        self.custom_note = note
        print("Customization applied.")

    def get_description(self) -> str:
        desc = f"{self.size} {self.name} - ${self.price:.2f}"
        if not self.ice:
            desc += " | No Ice"
        if not self.sugar:
            desc += " | No Sugar"
        if self.custom_note:
            desc += f" | Note: {self.custom_note}"
        return desc

class Order:
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 1.0

    def __init__(self):
        self.drinks: List[Drink] = []
        self.total: float = 0.0
        self.discount_applied: bool = False
        self.order_id: int = random.randint(1000, 9999)
        self.loyalty_points: int = 0
        self.payment_method: str = ""

    def add_drink(self, drink: Drink):
        self.drinks.append(drink)
        self._recalculate_total()

    def _recalculate_total(self):
        self.total = sum(d.price for d in self.drinks)
        if len(self.drinks) > self.DISCOUNT_THRESHOLD:
            self.total -= self.DISCOUNT_AMOUNT
            self.discount_applied = True
        else:
            self.discount_applied = False

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for d in self.drinks:
            print(d.get_description())
        print(f"Total: ${self.total:.2f}")
        if self.discount_applied:
            print("Discount applied!")
        print(f"Paid with: {self.payment_method}")

    def pay(self, method: str):
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
    def __init__(self, name: str):
        self.name = name
        self.orders_served: int = 0
        self.current_order: Optional[Order] = None

    def take_order(self, order: Order):
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