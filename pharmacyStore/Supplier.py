class Supplier:
    def __init__(self, supplier_id, name, address, phone_number):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.products = []

    def add_product(self, product):
        self.products.append(product)