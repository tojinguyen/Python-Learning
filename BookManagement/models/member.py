class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] 

    def __repr__(self):
        return f"Member({self.member_id}, {self.name}, {self.borrowed_books})"

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        self.borrowed_books.remove(book_id)