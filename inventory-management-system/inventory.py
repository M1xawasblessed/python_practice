from product import Product


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price):
        product = Product(name, quantity, price)
        self.products.append(product)

    def show_products(self):

        if not self.products:
            print("\nInventory is empty.")
            return

        print("\n===== PRODUCTS =====")

        for index, product in enumerate(self.products, start=1):
            print(
                f"{index}. {product.name} | Qty: {product.quantity} | €{product.price}"
            )