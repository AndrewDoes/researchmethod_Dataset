from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    category: str
    price: str
    stock: str
    tax: int = field(init=False)

    def __post_init__(self):
        self.tax = ProductManager.calculate_tax(self.category)

class ProductManager:
    def __init__(self):
        self.products: List[Product] = []

    @staticmethod
    def calculate_tax(category: str) -> int:
        if category == "Electronics":
            return 18
        elif category == "Clothing":
            return 5
        elif category == "Food":
            return 12
        else:
            return 8

    def add_product(self):
        print("Add Product")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")
        product = Product(name, category, price, stock)
        self.products.append(product)
        print("Product Added!")

    def display_products(self):
        print("\n--- Product List ---")
        for p in self.products:
            print(f"Name: {p.name}, Category: {p.category}, Price: {p.price}, Stock: {p.stock}, Tax: {p.tax}%")

    def update_product(self):
        prod_name = input("Enter product name to update: ")
        for p in self.products:
            if p.name == prod_name:
                p.category = input("Enter new category: ")
                p.price = input("Enter new price: ")
                p.stock = input("Enter new stock quantity: ")
                p.tax = self.calculate_tax(p.category)
                print("Product Updated!")
                return
        print("Product not found!")

    def delete_product(self):
        prod_name = input("Enter product name to delete: ")
        original_count = len(self.products)
        self.products = [p for p in self.products if p.name != prod_name]
        if len(self.products) < original_count:
            print("Product Deleted!")
        else:
            print("Product not found!")

    def main_menu(self):
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

def main():
    manager = ProductManager()
    manager.main_menu()

if __name__ == "__main__":
    main()