class Accounting:
    def __init__(self):
        self.products = []


class Product(Accounting):
    def __init__(self, name):
        super().__init__()
        self.name = name
        

class Customer(Product):
    def __init__(self, name):
        super().__init__("")
        self.name = name


accounting = Accounting()
cola = Product("Cola")
ivan = Customer("Ivan")
