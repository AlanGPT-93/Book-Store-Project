from utilis import database

USER_CHOICE = """\n Hi my dear user, I'll show you the menu:

- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to close the application

Please, type an option: """




def menu():
    user_choise = str(input(USER_CHOICE))

    while user_choise != "q":
        
        if user_choise == "a":
            book_name = str(input("Please enter the Book's name: "))
            book_author = str(input("Please enter the Book's author: "))
            database.add_book(book_name, book_author)
            user_choise = str(input(USER_CHOICE))

        elif user_choise == "r":
            book_name = str(input("Please enter the Book's name: "))
            book_author = str(input("Please enter the Book's author: "))
            database.mark_as_read(book_name, book_author)
            user_choise = str(input(USER_CHOICE))

        elif user_choise == "d":
            book_name = str(input("Please enter the Book's name: "))
            book_author = str(input("Please enter the Book's author: "))
            database.delete_book(book_name, book_author)
            user_choise = str(input(USER_CHOICE))
        
        elif user_choise == "l":
            database.list_books()
            user_choise = str(input(USER_CHOICE))
        
        else:
            user_choise = str(input(USER_CHOICE))

menu()