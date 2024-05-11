class Order:
    def __init__(self, order_id, date, client_id, employee_id, supplier_id):
        self.order_id = order_id
        self.date = date
        self.client_id = client_id
        self.employee_id = employee_id
        self.supplier_id = supplier_id
        self.order_details = []

    def add_order_detail(self, order_detail):
        self.order_details.append(order_detail)
