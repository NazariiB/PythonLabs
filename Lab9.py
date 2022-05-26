class Accounting:
    def __init__(self):
        self.products = []

    def __str__(self):
        return f"Accounting: {self.products}"


class Product(Accounting):
    def __init__(self, product_id):
        super().__init__()
        self.id = product_id

    def __str__(self):
        return f"Product id: {self.id}"


class Customer(Product):
    def __init__(self, name, product_id):
        super().__init__(product_id)
        self.name = name

    def __str__(self):
        return f"Customer name: {self.name}"


accounting = Accounting()
print(accounting)
cola = Product(105)
print(cola)
ivan = Customer("Ivan", 105)
print(ivan)
