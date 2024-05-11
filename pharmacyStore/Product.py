import copy

class Product:
    def __init__(self, product_id, name, description, price, stock_quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity
        self.supplier_id = supplier_id

    def clone(self):
        return copy.deepcopy(self)