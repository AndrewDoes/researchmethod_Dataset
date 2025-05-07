class Store:
    def __init__(self):
        self.users = []
        self.products = []
        self.tax_rate = 0.08

    def register_user(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append((name, age, email))
        print("User registered!")

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        self.products.append({"name": name, "price": price, "stock": stock})

    def display_products(self):
        print("\n--- Product List ---")
        for product in self.products:
            print(f"{product['name']} - ${product['price']:.2f} ({product['stock']} left)")

    def find_product(self, name):
        for product in self.products:
            if product["name"] == name:
                return product
        return None

    def purchase(self):
        name = input("Enter product name: ")
        product = self.find_product(name)
        if product is None:
            print("Product not found!")
            return
        qty = int(input("Enter quantity: "))
        if product["stock"] < qty:
            print("Not enough stock!")
            return
        product["stock"] -= qty
        total = product["price"] * qty
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total + (total * self.tax_rate):.2f}")

    def main_menu(self):
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


if __name__ == "__main__":
    store = Store()
    store.main_menu()

