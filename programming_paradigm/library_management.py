


class Book:
    """Class to represent a book in the library."""

    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Cannot check out an already checked-out book

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Cannot return a book that is not checked out

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Class to manage a collection of books."""

    def __init__(self):
        """Initialize the library with an empty book collection."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only instances of Book can be added.")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
