from utilis import database

USER_CHOICE = """\n Hi my dear user, I'll show you the menu:

- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to close the application

Please, type an option: """

user_action = {
    "a": database.add_book,
    "l": database.list_books,
    "r": database.mark_as_read,
    "d": database.delete_book
}


def menu():
    user_choise = str(input(USER_CHOICE))

    while user_choise != "q":

        if user_choise in ["a","r","d"]:
            book_name = str(input("Please enter the Book's name: "))
            book_author = str(input("Please enter the Book's author: "))
            user_action[user_choise](book_name,book_author)

        elif user_choise == "l":
            user_action[user_choise]()

        elif user_choise == "q":
            break

        else:
            user_choise = str(input(USER_CHOICE))
        
        user_choise = str(input(USER_CHOICE))

menu()

