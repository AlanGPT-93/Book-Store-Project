"""
Concerned with storing and retrieving books from a list. 

"""

#import sqlite3
from .context_manager import DataConnection

def create_table():
    with DataConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE Table IF NOT EXISTS books(name text pk, author text, read int16 ) ")

def add_book(book_name,book_author):
    with DataConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books values(?,?,0)",(book_name, book_author) )
    
def list_books():
    with DataConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("select * from books" )
        books = cursor.fetchall()
    
    for i, (book_name, book_author, read) in enumerate(books):
        print(f"\n {i+1}- {book_name} by {book_author}, read = {read}")

def delete_book(book_name, book_author):
    with DataConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE from books WHERE name=? and author=?",(book_name, book_author) )
    
def mark_as_read(book_name, book_author):
    with DataConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=? and author=?",(book_name, book_author) )
    