class Store:
    TAX_RATE = 0.08

    def __init__(self):
        self.users = []
        self.products = []

    def register_user(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append((name, age, email))
        print("User registered!")

    def add_product(self):
        name = input("Enter product name: ")
        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            self.products.append((name, price, stock))
        except ValueError:
            print("Invalid input. Please enter numeric values for price and stock.")

    def display_products(self):
        print("\n--- Product List ---")
        for name, price, stock in self.products:
            print(f"{name} - ${price:.2f} ({stock} left)")

    def find_product_index(self, name):
        for i, (prod_name, _, _) in enumerate(self.products):
            if prod_name == name:
                return i
        return -1

    def purchase(self):
        name = input("Enter product name: ")
        index = self.find_product_index(name)
        if index == -1:
            print("Product not found!")
            return
        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity!")
            return
        product_name, price, stock = self.products[index]
        if stock < qty:
            print("Not enough stock!")
            return
        self.products[index] = (product_name, price, stock - qty)
        total = price * qty
        total_with_tax = total * (1 + self.TAX_RATE)
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total_with_tax:.2f}")

    def menu(self):
        while True:
            print("\n1. Register\n2. Add Product\n3. View Products\n4. Purchase\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.display_products()
            elif choice == "4":
                self.purchase()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


def main():
    store = Store()
    store.menu()


if __name__ == "__main__":
    main()