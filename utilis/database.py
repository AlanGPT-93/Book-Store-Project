"""
Concerned with storing and retrieving books from a list. 

"""

books = []


def add_book(book_name, book_author):
    books.append({"Name":book_name, "Author":book_author, "Read":False })

def list_books():
    print(books)

def delete_book(book_name, book_author):
    pass

def mark_as_read(book_name, book_author):
    for book in books:
        if book["Name"] == book_name and book["Author"] == book_author:
            book["Read"] = True
            break