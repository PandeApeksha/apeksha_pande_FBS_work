class Book:
    count = 0
    def __init__(self, id = 1, name = 'mrityunjay', price = 500, author = 'shivaji savant'):
        self.bid = id
        self.bname = name
        self.price = price
        self.author = author
        Book.count += 1
        
    def __del__(self):
        Book.count -= 1
        print(f'distructor is called for Book ID :{self.bid}')

    def ShowBook(self):
        return f'ID:{self.bid}\nNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}'
    
    def totalBook():
        print(f'Total Books :{Book.count}')
    
    

book1 = Book()
print(book1.ShowBook())
print()

book2 = Book(2, 'yayati', 1000, 'V. S. khandekar')
print(book2.ShowBook())
print()

Book.totalBook()

del book1

Book.totalBook()


