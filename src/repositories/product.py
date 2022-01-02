import json


class ProductRepository:
    products = None

    def __init__(self):
        self.load_data()

    def load_data(self):
        with open(f'src/repositories/data/products.json') as json_products:
            self.products = json.load(json_products)

    def get_products(self):
        return self.products
