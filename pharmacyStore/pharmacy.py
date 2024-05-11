from Order import Order
from Client import Client
from Employee import Employee
from Supplier import Supplier
from OrderBuilder import OrderBuilder

class Pharmacy:
    def __init__(self):
        self.inventory = {}
        self.clients = []
        self.employees = []
        self.suppliers = []

    def add_product(self, product):
        self.inventory[product.product_id] = product

    def add_client(self, client):
        self.clients.append(client)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def show_inventory(self):
        print("Inventory:")
        for product_id, product in self.inventory.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Stock: {product.stock_quantity}, Supplier ID: {product.supplier_id}")

    def place_order(self):
        order_builder = OrderBuilder()
        order_builder.set_order_id(input("Enter order ID: "))
        order_builder.set_date(input("Enter order date (YYYY-MM-DD): "))

        client_id = input("Enter client ID: ")
        employee_id = input("Enter employee ID: ")
        supplier_id = input("Enter supplier ID: ")

        order_builder.set_client_id(client_id)
        order_builder.set_employee_id(employee_id)
        order_builder.set_supplier_id(supplier_id)

        while True:
            product_id = input("Enter product ID to purchase (0 to finish): ")
            if product_id == '0':
                break
            quantity = int(input("Enter quantity: "))
            if product_id in self.inventory:
                product = self.inventory[product_id]
                if quantity <= product.stock_quantity:
                    order_builder.add_order_detail((product_id, quantity, product.price))
                    product.stock_quantity -= quantity
                else:
                    print("Insufficient stock available!")
            else:
                print("Product not found in inventory.")

        order = order_builder.build()
        if order.order_details:
            print("Order placed successfully.")
            return order
        else:
            print("Empty order, no purchase was made.")
            return None

    def show_order_details(self, order):
        print("\nOrder Details:")
        print(f"Order ID: {order.order_id}")
        print(f"Order Date: {order.date}")
        print(f"Client: {order.client_id}")
        for product_id, quantity, price in order.order_details:
            product = self.inventory[product_id]
            print(f"Product ID: {product_id}, Name: {product.name}, Quantity: {quantity}, Price: {price}")
