class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an eBook, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # File size in KB (adjusted)
    def __str__(self):
            return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that manages a collection of books using composition.
    """
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
