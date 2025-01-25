class Book:

    def __init__(self, title, autor, year):

        self.title = title
        self.autor = autor
        self.year = year


    def __del__(self):

        print(f"Deleting {self.title}")


    def __str__(self):


        return f"{self.title} by {self.autor}, published in {self.year}"



    def __rpr__(self):

        return f"Book('{self.title}', '{self.author}', {self.year})"