import json


def save_products(products):

    data = []

    for product in products:
        data.append(product.to_dict())

    with open("products.json", "w") as file:
        json.dump(data, file, indent=4)


def load_products():

    try:

        with open("products.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []