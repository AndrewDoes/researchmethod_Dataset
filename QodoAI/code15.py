class Product:
    TAX_RATES = {
        "Electronics": 18,
        "Clothing": 5,
        "Food": 12
    }

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        return self.TAX_RATES.get(self.category, 8)

    def update(self, category, price, stock):
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax()

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}, Tax: {self.tax}%"

class ProductManagementSystem:
    def __init__(self):
        self.products = []

    def add_product(self):
        print("Add Product")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")

        self.products.append(Product(name, category, price, stock))
        print("Product Added!")

    def display_products(self):
        print("\n--- Product List ---")
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product)

    def update_product(self):
        prod_name = input("Enter product name to update: ")
        for product in self.products:
            if product.name == prod_name:
                category = input("Enter new category: ")
                price = input("Enter new price: ")
                stock = input("Enter new stock quantity: ")
                product.update(category, price, stock)
                print("Product Updated!")
                return
        print("Product not found!")

    def delete_product(self):
        prod_name = input("Enter product name to delete: ")
        self.products = [product for product in self.products if product.name != prod_name]
        print("Product Deleted!")

    def main_menu(self):
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

    def exit_program(self):
        print("Exiting...")
        exit()

if __name__ == "__main__":
    system = ProductManagementSystem()
    system.main_menu()