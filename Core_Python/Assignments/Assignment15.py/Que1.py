class Book:
    def __init__(self, id = 1, name = 'mrityunjay', price = 500, author = 'shivaji savant'):
        self.bid = id
        self.bname = name
        self.price = price
        self.author = author

    def ShowBook(self):
        return f'ID:{self.bid}\nNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}'
    
    def __del__(self):
        print('distructor is called')

book1 = Book()
print(book1.ShowBook())
print()

book2 = Book(2, 'yayati', 1000, 'V. S. khandekar')
print(book2.ShowBook())
print()