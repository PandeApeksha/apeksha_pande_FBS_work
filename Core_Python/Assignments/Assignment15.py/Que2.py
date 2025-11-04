class Product:
    def __init__(self, id = 1, name = 'chair', price = 2000, quantity = 6):
        self.pid = id
        self.pname = name
        self.price = price
        self.quantity = quantity

    def ShowProduct(self):
        return f'ID:{self.pid}\nNAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}'
    
    def __del__(self):
        print('distructor is called')

book1 = Product()
print(book1.ShowProduct())
print()

book2 = Product(2, 'Table', 4500, 3)
print(book2.ShowProduct())
print()