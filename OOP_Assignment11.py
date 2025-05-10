"""11. Class Methods
Assignment:
Create a class Book with a class variable total_books.
Add a class method increment_book_count() to increase the count when a new book is added."""

class Book:
    total_books = 0

    def __init__(self,title):
        self.title = title
        Book.increment_book_count()
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1    
# additional  
    def __del__(self):
        Book.total_books = Book.total_books - 1    

book1 = Book("My book1")        
book2 = Book("My book2")        
book3 = Book("My book3")        
del book1
print(Book.total_books)