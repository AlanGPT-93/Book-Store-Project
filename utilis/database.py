"""
Concerned with storing and retrieving books from a list. 

"""

import sqlite3

def create_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("CREATE Table IF NOT EXISTS books(name text pk, author text, read int16 ) ")
    connection.commit()
    connection.close()

def add_book(book_name,book_author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books values(?,?,?)",(book_name, book_author, 0) )
    connection.commit()
    connection.close()

def list_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("select * from books" )
    books = cursor.fetchall()
    connection.close()
    for i, (book_name, book_author, read) in enumerate(books):
        print(f"\n {i+1}- {book_name} by {book_author}, read = {read}")

def delete_book(book_name, book_author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from books WHERE name=? and author=?",(book_name, book_author) )
    connection.commit()
    connection.close()

def mark_as_read(book_name, book_author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET read=1 WHERE name=? and author=?",(book_name, book_author) )
    connection.commit()
    connection.close()