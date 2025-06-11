class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, searched_title):
        found = False
        for book in self.books:
            if book.title == searched_title and book.is_borrowed == False:
                book.is_borrowed = True
                found = True
                print(f"You just borrowed {searched_title}")
            elif book.is_borrowed == True:
                print("Book is borrowed") 
        if found == False:
            print("Book doesn't exist.")
        if book.is_borrowed == True:
            print("Book is borrowed")
            return


    def return_book(self, searched_title):
        for book in self.books:
            if book.title == searched_title and book.is_borrowed == True:
                book.is_borrowed = False
                print(f"You just returned {searched_title}")
                return


    def list_available_books(self):
        print("\nAvailable books:")
        for book in self.books:
            if book.is_borrowed == False:
                print(f"- {book.title} by {book.author}")

library = Library()

book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

library.add_book(book1)
library.add_book(book2)

library.borrow_book("1984")
library.borrow_book("1985")
library.borrow_book("1984")
library.list_available_books()

library.return_book("1984")
library.list_available_books()