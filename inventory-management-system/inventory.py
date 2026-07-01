from product import Product
from storage import save_products, load_products


class Inventory:

    def __init__(self):

        self.products = []

        data = load_products()

        for item in data:

            product = Product(
                item["name"],
                item["quantity"],
                item["price"]
            )

            self.products.append(product)

    def add_product(self, name, quantity, price):

        product = Product(name, quantity, price)

        self.products.append(product)

        save_products(self.products)

    def show_products(self):

        if not self.products:
            print("\nInventory is empty.")
            return

        print("\n===== PRODUCTS =====")

        for index, product in enumerate(self.products, start=1):
            print(
                f"{index}. {product.name} | Qty: {product.quantity} | €{product.price}"
            )