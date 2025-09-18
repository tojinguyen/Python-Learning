from models.book import Book
from models.member import Member
from management.library import Library

library = Library()

while True:
    print(""" ===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. Delete Book
8. Delete Member
9. Find Book
10. Find Member
0. Exit
=====================================""")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year: ")
            quantity = int(input("Enter Quantity: "))
            book = Book(book_id, title, author, year, quantity)
            library.add_book(book)
            print("Book added successfully.")

        case 2:
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            member = Member(member_id, name)
            library.add_member(member)
            print("Member added successfully.")

        case 3:
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            if library.borrow_book(member_id, book_id):
                print("Book borrowed successfully.")
            else:
                print("Failed to borrow book. Check member ID, book ID, and availability.")
        case 4:
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            if library.return_book(member_id, book_id):
                print("Book returned successfully.")
            else:
                print("Failed to return book. Check member ID and book ID.")
        case 5:
            print("Books:")
            for book in library.books:
                print(book)
        case 6:
            print("Members:")
            for member in library.members:
                print(member)
        case 7:
            book_id = input("Enter Book ID to delete: ")
            for book in library.books:
                if book.book_id == book_id:
                    library.books.remove(book)
                    print("Book deleted successfully.")
                    break
            else:
                print("Book not found.")
        case 8:
            member_id = input("Enter Member ID to delete: ")
            for member in library.members:
                if member.member_id == member_id:
                    library.members.remove(member)
                    print("Member deleted successfully.")
                    break
                else:
                    print("Member not found.")
        case 9:
            book_id = input("Enter Book ID to find: ")
            book = library.find_book(book_id)
            if book:
                print(book)
            else:
                print("Book not found.")
        case 10:
            member_id = input("Enter Member ID to find: ")
            member = library.find_member(member_id)
            if member:
                print(member)
            else:
                print("Member not found.")
        case 0:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")



