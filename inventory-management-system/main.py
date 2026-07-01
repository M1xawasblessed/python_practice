from inventory import Inventory

inventory = Inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        # 🔹 Product name
        name = input("Product Name: ")

        # 🔹 Quantity validation
        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity < 0:
                    print("❌ Quantity cannot be negative!")
                    continue
                break
            except ValueError:
                print("❌ Enter a valid integer!")

        # 🔹 Price validation (FIXED PART)
        while True:
            price_input = input("Price (€): ").replace("$", "").replace("€", "")
            try:
                price = float(price_input)
                if price < 0:
                    print("❌ Price cannot be negative!")
                    continue
                break
            except ValueError:
                print("❌ Invalid price! Please enter like 55.99")

        # 🔹 Add product
        inventory.add_product(name, quantity, price)

        print("✅ Product added successfully!")

    elif choice == "2":

        inventory.show_products()

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")