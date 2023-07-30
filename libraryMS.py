class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Available books in the library:")
        for book in self.books:
            if book.is_available:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book '{book.title}'.")
        else:
            print(f"The book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book '{book.title}'.")
        else:
            print(f"{self.name} did not borrow the book '{book.title}'.")

def main():
    library = Library()

    book1 = Book("Python Crash Course", "Eric Matthes", "101")
    book2 = Book("The Alchemist", "Paulo Coelho", "102")
    book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "103")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_books()

    borrower1 = Borrower("John")
    borrower2 = Borrower("Alice")

    book_to_borrow = library.find_book_by_id("101")
    borrower1.borrow_book(book_to_borrow)

    book_to_borrow = library.find_book_by_id("102")
    borrower2.borrow_book(book_to_borrow)

    book_to_return = library.find_book_by_id("102")
    borrower2.return_book(book_to_return)

    library.display_books()

if __name__ == "__main__":
    main()
