class Product:
    discount = 0
    def __init__(self, id = 1, name = 'laptop', price = 60000, quantity = 1):
        self.pid = id
        self.pname = name
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f'destructor called for product :{self.pname}')

    def showProduct(self):
        print(f'ID :{self.pid}')
        print(f'NAME :{self.pname}')
        print(f'PRICE :{self.price}')
        print(f'QUANTITY :{self.quantity}')
        print(f'DISCOUNT :{Product.discount}%')
        print(f'price after discount :{self.price_after_discount()}')    

    def set_discount(self, d):
        Product.discount = d

    def price_after_discount(self):
        discount_price = (self.price) - (self.price * Product.discount / 100)
        return discount_price
    
product1 = Product(2, 'smartphone', 800000, 1)
product1.set_discount(10)
product1.showProduct()
print()

product2 = Product(3, 'earbuds', 3000, 3)
product2.set_discount(20)
product2.showProduct()
print()

product3 = Product()
product3.showProduct()
print()

del product1
    

    


