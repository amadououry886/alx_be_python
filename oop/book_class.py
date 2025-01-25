class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance with title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the Book object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance for user-friendly display.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance for debugging and recreating the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
