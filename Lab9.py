class Accounting:
    def __init__(self):
        self.products = []


class Product(Accounting):
    def __init__(self, product_id):
        super().__init__()
        self.id = product_id


class Customer(Product):
    def __init__(self, name, product_id):
        super().__init__(product_id)
        self.name = name


accounting = Accounting()
cola = Product(105)
ivan = Customer("Ivan", 105)
