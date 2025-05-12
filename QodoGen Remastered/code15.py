class Product:
    TAX_RATES = {
        "Electronics": 18,
        "Clothing": 5,
        "Food": 12,
        "Other": 8
    }

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.TAX_RATES.get(category, self.TAX_RATES["Other"])

    def update(self, category, price, stock):
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.TAX_RATES.get(category, self.TAX_RATES["Other"])

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}, Tax: {self.tax}%"


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        print("Add Product")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")

        new_product = Product(name, category, price, stock)
        self.products.append(new_product)
        print("Product Added!")

    def display_products(self):
        print("\n--- Product List ---")
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

    def menu(self):
        while True:
            print("\n1. Add Product\n2. Display Products\n3. Update Product\n4. Delete Product\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.display_products()
            elif choice == "3":
                self.update_product()
            elif choice == "4":
                self.delete_product()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    manager = ProductManager()
    manager.menu()