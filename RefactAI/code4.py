users = []
products = []
tax = 0.08

def register():
    global users
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    users.append((name, age, email))
    print("User registered!")

def addProduct():
    global products
    name = input("Enter product name: ")
    price = input("Enter price: ")
    stock = input("Enter stock quantity: ")
    products.append((name, float(price), int(stock)))

def displayProducts():
    global products
    print("\n--- Product List ---")
    for i in range(len(products)):
        print(f"{products[i][0]} - ${products[i][1]:.2f} ({products[i][2]} left)")

def findProduct(name):
    global products
    for i in range(len(products)):
        if products[i][0] == name:
            return i
    return -1

def purchase():
    global products
    name = input("Enter product name: ")
    index = findProduct(name)
    if index == -1:
        print("Product not found!")
        return
    qty = int(input("Enter quantity: "))
    if products[index][2] < qty:
        print("Not enough stock!")
        return
    products[index] = (products[index][0], products[index][1], products[index][2] - qty)
    total = products[index][1] * qty
    print(f"Total: ${total:.2f}")
    print(f"Total with tax: ${total + (total * tax):.2f}")

def menu():
    while True:
        print("\n1. Register\n2. Add Product\n3. View Products\n4. Purchase\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            addProduct()
        elif choice == "3":
            displayProducts()
        elif choice == "4":
            purchase()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()
