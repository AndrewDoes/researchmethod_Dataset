import random
from enum import Enum
from typing import List, Optional

class DrinkSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class PaymentMethod(Enum):
    CASH = "Cash"
    CREDIT_CARD = "Credit Card"
    E_WALLET = "E-Wallet"
    OTHER = "Other"

class Drink:
    """Represents a drink with customizable options."""
    def __init__(self, name: str, size: DrinkSize, price: float, ice: bool = True, sugar: bool = True):
        self.name = name
        self.size = size
        self.price = price
        self.ice = ice
        self.sugar = sugar
        self.custom_note = ""

    def customize(self, ice: bool, sugar: bool, note: str = "") -> None:
        """Customize the drink's ice, sugar, and add a note."""
        self.ice = ice
        self.sugar = sugar
        self.custom_note = note
        print("Customization applied.")

    def get_description(self) -> str:
        """Return a string description of the drink."""
        desc = f"{self.size.value} {self.name} - ${self.price:.2f}"
        if not self.ice:
            desc += " | No Ice"
        if not self.sugar:
            desc += " | No Sugar"
        if self.custom_note:
            desc += f" | Note: {self.custom_note}"
        return desc

class Order:
    """Represents a customer's order, which may contain multiple drinks."""
    DISCOUNT_THRESHOLD = 3
    DISCOUNT_AMOUNT = 1.0

    def __init__(self):
        self.drinks: List[Drink] = []
        self.total: float = 0.0
        self.discount_applied: bool = False
        self.order_id: int = random.randint(1000, 9999)
        self.loyalty_points: int = 0
        self.payment_method: Optional[PaymentMethod] = None

    def add_drink(self, drink: Drink) -> None:
        """Add a drink to the order and update the total."""
        self.drinks.append(drink)
        self.total += drink.price
        self._apply_discount_if_eligible()

    def _apply_discount_if_eligible(self) -> None:
        """Apply a discount if the number of drinks exceeds the threshold."""
        if len(self.drinks) > self.DISCOUNT_THRESHOLD and not self.discount_applied:
            self.total -= self.DISCOUNT_AMOUNT
            self.discount_applied = True

    def print_order(self) -> None:
        """Print the order details."""
        print(f"Order ID: {self.order_id}")
        for drink in self.drinks:
            print(drink.get_description())
        print(f"Total: ${self.total:.2f}")
        if self.discount_applied:
            print("Discount applied!")
        print(f"Paid with: {self.payment_method.value if self.payment_method else 'Not paid'}")

    def pay(self, method: PaymentMethod) -> None:
        """Process payment and update loyalty points."""
        self.payment_method = method
        self.loyalty_points += int(self.total // 2)
        print("Payment successful.")

    def cancel_order(self) -> None:
        """Cancel the order and reset all fields."""
        self.drinks.clear()
        self.total = 0.0
        self.discount_applied = False
        self.payment_method = None
        self.loyalty_points = 0
        print("Order cancelled.")

class Barista:
    """Represents a barista who can take and serve orders."""
    def __init__(self, name: str):
        self.name = name
        self.orders_served: int = 0
        self.current_order: Optional[Order] = None

    def take_order(self, order: Order) -> None:
        """Assign an order to the barista."""
        self.current_order = order
        print(f"{self.name} took the order.")

    def serve_order(self) -> None:
        """Serve the current order."""
        if self.current_order:
            self.orders_served += 1
            print("Order served.")
            self.current_order = None

    def report(self) -> None:
        """Print a report of orders served."""
        print(f"Barista {self.name} served {self.orders_served} orders today.")

def main():
    drink1 = Drink("Green Tea", DrinkSize.MEDIUM, 3.5)
    drink2 = Drink("Latte", DrinkSize.LARGE, 4.5)
    drink2.customize(ice=False, sugar=True, note="Extra hot")

    order = Order()
    order.add_drink(drink1)
    order.add_drink(drink2)
    order.pay(PaymentMethod.CREDIT_CARD)
    order.print_order()

    barista = Barista("Lina")
    barista.take_order(order)
    barista.serve_order()
    barista.report()

if __name__ == "__main__":
    main()