from inventory import Inventory

inventory = Inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Product Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price (€): "))

        inventory.add_product(name, quantity, price)

        print("Product added successfully!")

    elif choice == "2":

        inventory.show_products()

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid option.")