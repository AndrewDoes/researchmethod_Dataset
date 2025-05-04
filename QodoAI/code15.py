class Product:
    TAX_RATES = {
        "Electronics": 18,
        "Clothing": 5,
        "Food": 12
    }

    def __init__(self, name: str, category: str, price: float, stock: int) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.TAX_RATES.get(category, 8)

    def update(self, category: str, price: float, stock: int) -> None:
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.TAX_RATES.get(category, 8)

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}, Tax: {self.tax}%"


class ProductManagementSystem:
    def __init__(self) -> None:
        self.products = []

    def add_product(self) -> None:
        print("Add Product")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        self.products.append(Product(name, category, price, stock))
        print("Product Added!")

    def display_products(self) -> None:
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def update_product(self) -> None:
        prod_name = input("Enter product name to update: ")
        product = self._find_product(prod_name)
        if product:
            category = input("Enter new category: ")
            price = float(input("Enter new price: "))
            stock = int(input("Enter new stock quantity: "))
            product.update(category, price, stock)
            print("Product Updated!")
        else:
            print("Product not found!")

    def delete_product(self) -> None:
        prod_name = input("Enter product name to delete: ")
        self.products = [p for p in self.products if p.name != prod_name]
        print("Product Deleted!")

    def _find_product(self, name: str) -> Product:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def menu(self) -> None:
        actions = {
            "1": self.add_product,
            "2": self.display_products,
            "3": self.update_product,
            "4": self.delete_product,
            "5": self.exit_program
        }
        while True:
            print("\n1. Add Product\n2. Display Products\n3. Update Product\n4. Delete Product\n5. Exit")
            choice = input("Enter choice: ")
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, try again.")

    def exit_program(self) -> None:
        print("Exiting...")
        exit()


if __name__ == "__main__":
    system = ProductManagementSystem()
    system.menu()