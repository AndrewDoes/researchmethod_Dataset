products = []

def add_product():
    print("Add Product")
    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = input("Enter price: ")
    stock = input("Enter stock quantity: ")

    if category == "Electronics":
        tax = 18
    elif category == "Clothing":
        tax = 5
    elif category == "Food":
        tax = 12
    else:
        tax = 8

    products.append({"name": name, "category": category, "price": price, "stock": stock, "tax": tax})
    print("Product Added!")

def display_products():
    print("\n--- Product List ---")
    for p in products:
        print(f"Name: {p['name']}, Category: {p['category']}, Price: {p['price']}, Stock: {p['stock']}, Tax: {p['tax']}%")

def update_product():
    prod_name = input("Enter product name to update: ")
    for p in products:
        if p['name'] == prod_name:
            p['category'] = input("Enter new category: ")
            p['price'] = input("Enter new price: ")
            p['stock'] = input("Enter new stock quantity: ")

            if p['category'] == "Electronics":
                p['tax'] = 18
            elif p['category'] == "Clothing":
                p['tax'] = 5
            elif p['category'] == "Food":
                p['tax'] = 12
            else:
                p['tax'] = 8

            print("Product Updated!")
            return
    print("Product not found!")

def delete_product():
    prod_name = input("Enter product name to delete: ")
    global products
    products = [p for p in products if p['name'] != prod_name]
    print("Product Deleted!")

def main():
    while True:
        print("\n1. Add Product\n2. Display Products\n3. Update Product\n4. Delete Product\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

main()
