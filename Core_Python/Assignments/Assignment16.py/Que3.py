class Shirt:

    def __init__(self, id = 1, name = 'white shirt', type = 'formal', price = 1000, size = 'small'):
        self.sid = id
        self.sname = name
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f'destructor is called for shirt id :{self.sid}')

    def showshirt(self):
        print(f'ID :{self.sid}')
        print(f'NAME :{self.sname}')
        print(f'TYPE :{self.type}')
        print(f'PRICE :{self.price}')
        print(f'SIZE :{self.size}')
        print(f'final price :{self.Price_according_size()}')


    def Price_according_size(self):
        if self.size == 'small':
            increase_percent = 0
        elif self.size == 'medium':
            increase_percent = 10
        elif self.size == 'large':
            increase_percent = 20
        elif self.size == 'xlarge':
            increase_percent = 30
        else:
            increase_percent = 0 

        Final_price = self.price + (self.price * increase_percent / 100)
        return Final_price

shirt1 = Shirt()
shirt1.showshirt()
print()

shirt2 = Shirt(2, "Black Shirt", "casual", 1200, "large")
shirt2.showshirt()
print()
