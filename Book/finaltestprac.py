"""
Exercise 1. (5pt)
Create a Python class called LibraryBook with the following attributes:

title: representing the book title.

author: representing the author name.

available: a boolean indicating whether the book is available or borrowed.

Create an instance of the LibraryBook class with the following details:

Title: 1984  
Author: George Orwell  
Available: True  

Add an instance method borrow() that:
- Changes the book status to borrowed if it is available.
- Prints an appropriate message if the book is already borrowed.


Exercise 2. (5pt)
Define a subclass called SpecialEditionBook inheriting from the LibraryBook class.
Add an additional attribute:

extras: representing special features of the book (e.g., illustrations, notes).

Override the borrow() method so that:
- It performs the normal borrowing behavior.
- It also prints out the extras information when the book is successfully borrowed.


Exercise 3. (5pt)
Add an instance method called save_to_file(filename) to the SpecialEditionBook class.
This method should:

- Save the book's title, author, availability status, and extras to a text file.
- Each piece of information must be written on a separate line.
- Properly handle exceptions using try-except in case any file-related error occurs.


Exercise 4. (5pt)
Add an instance method called save_in_background(filename) to the SpecialEditionBook class.
This method should:

- Create a separate thread using the threading module.
- Call the save_to_file(filename) method inside the new thread.

In the main thread, create an instance of SpecialEditionBook and call save_in_background()
to save the book information into a file named "book_info.txt".

"""
import threading

class LibraryBook:
    def __init__(self,title,author,available):
        self.title = title
        self.author = author
        self.available = available
    def borrow_book(self):
        if (self.available):
            print("Borrow book")
            self.available = False
        else:
            print("Can't Borrow book")
b1 = LibraryBook("1984","George Orwell ",True)

class SpecialEditionBook(LibraryBook):
    def __init__(self,title,author,available,extras):
        super().__init__(title,author,available)
        self.extras = extras
    def borrow_book(self):
        if (self.available):
            print("Borrow book")
            print(self.extras)
            self.available = False
        else:
            print("Can't Borrow book")
    def save_to_file(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(self.title + "\n" + self.author + "\n" + str(self.available) + "\n" + str(self.extras))
        except Exception:
            print("Exception")
    def save_to_background(self,filename):
        t = threading.Thread(target=self.save_to_file,args=(filename,))
        t.start()
b2 = SpecialEditionBook("ABC","DEF",True,["Signature","Illustrations"])
b2.save_to_background("output.txt")

        