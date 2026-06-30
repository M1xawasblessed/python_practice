class Product:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }