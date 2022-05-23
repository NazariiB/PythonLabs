class Accounting:
    def __init__(self):
        self.products = []


class Product(Accounting):
    def __init__(self, name):
        super().__init__()
        self.name = name
C:\Users\nazik\PycharmProjects\pythonProject1\Lab9.py

class Customer(Product):
    def __init__(self, name):
        super().__init__("")
        self.name = name


accounting = Accounting()
cola = Product("Cola")
ivan = Customer("Ivan")
