class Shirt:
    def __init__(self, id = 1, name = 'formal shirt', type = 'formal', price = 700, size = 'XL'):
        self.pid = id
        self.pname = name
        self.type = type
        self.price = price
        self.size = size

    def ShowData(self):
        return f'ID:{self.pid}\nNAME:{self.pname}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}'
    
    def __del__(self):
        print('distructor is called')

book1 = Shirt()
print(book1.ShowData())
print()

book2 = Shirt(2, 'Denum shirt', 'Denim', 900, 'M')
print(book2.ShowData())
print()