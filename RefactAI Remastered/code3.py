items = []
taxRate = 0.1
discThresh = 100
discPerc = 0.05

def additem():
    global items
    name = input("Enter item name: ")
    p = input("Enter price: ")
    q = input("Enter quantity: ")
    items.append((name, float(p), int(q)))

def printItems():
    global items
    print("\n--- Items List ---")
    for i in range(len(items)):
        print(f"{items[i][0]} x{items[i][2]} - ${items[i][1] * items[i][2]:.2f}")

def calcTotal():
    global items
    total = 0
    for i in range(len(items)):
        total += items[i][1] * items[i][2]
    return total

def calcTax():
    global items
    total = 0
    for i in range(len(items)):
        total += items[i][1] * items[i][2]
    return total * taxRate

def applyDisc():
    global items
    total = 0
    for i in range(len(items)):
        total += items[i][1] * items[i][2]
    if total > discThresh:
        return total * (1 - discPerc)
    return total

def printReciept():
    global items
    total = calcTotal()
    tax = calcTax()
    discounted_price = applyDisc()
    final_total = discounted_price + tax

    print("\n--- Receipt ---")
    for i in range(len(items)):
        print(f"{items[i][0]} x{items[i][2]} - ${items[i][1] * items[i][2]:.2f}")
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${final_total:.2f}")

def main():
    while True:
        print("\n1. Add Item\n2. View Items\n3. Print Receipt\n4. Exit")
        c = input("Enter choice: ")
        if c == "1":
            additem()
        elif c == "2":
            printItems()
        elif c == "3":
            printReciept()
        elif c == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
