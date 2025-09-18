class Book:
    def __init__(self, book_id, title, author, year, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def __repr__(self):
        return f"Book({self.book_id}, {self.title}, {self.author}, {self.year}, {self.quantity})"