# Custom Exceptions
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"


# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def __str__(self):
        borrowed_titles = ', '.join(book.title for book in self.borrowed_books) or "No books borrowed"
        return f"Member: {self.name} | Borrowed Books: {borrowed_titles}"


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"{member_name} successfully borrowed '{book_title}'.")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"{member_name} successfully returned '{book_title}'.")
        except BookNotFoundException as e:
            print(e)

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)


# Test the Library System
library = Library()

# Adding Books
library.add_book(Book("Martin Eden", "Jack London"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Adding Members
library.add_member(Member("Charlie"))
library.add_member(Member("Carlos"))

# Display Books
print("\nAvailable Books:")
library.list_books()

# Borrowing Books
print("\nBorrowing Books:")
library.borrow_book("Charlie", "1984")
library.borrow_book("Carlos", "The Great Gatsby")
library.borrow_book("Carlos", "Martin Eden")

# Handling Exceptions
print("\nException Handling:")
library.borrow_book("Carlos", "Martin Eden")  # Book already borrowed
library.borrow_book("Carlos", "The count of Monte-Cristo")  # Book not found
library.borrow_book("Carlos", "Divine Comedy")  # Exceeds limit

# Display Members
print("\nLibrary Members:")
library.list_members()

# Returning Books
print("\nReturning Books:")
library.return_book("Carlos", "Martin Eden")

# Display Books After Return
print("\nUpdated Book List:")
library.list_books()
