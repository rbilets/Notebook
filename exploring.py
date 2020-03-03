import sys
from menu import Menu
from notebook import Notebook, Note

if __name__ == '__main__':

    # Exploring methods of a class
    print(dir(Menu))  # Displays all methods of a class Menu
    print(dir(Notebook))  # Displays all methods of a class Notebook
    print(dir(Note))  # Displays all methods of a class Note

    # Exploring attributes of a class:
    test_note = Note('Hello World', 'Greeting')  # Creating the object of class Note
    # __init__ method is automatically called when the instance is being created

    print(type(test_note))  # The object of Note class

    # Self represents the instance itself

    print(test_note.memo)  # Attribute of the object test_note, can be accessed using '.'
    print(test_note.tags)  # Attribute of the object test_note, can be accessed using '.'

    print(str(test_note))  # Prints information about the object
    # Method __str__ overrides the initial method in which you get info about the object with its location in memory






