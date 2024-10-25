class Library:
    def __init__(self): 
        self.author = []                                                            # Initialize instance variables
        self.books = []
        self.no_of_books = 0
   
    def add_book(self, book_name, author_name):                                     # Add a book and update count
        self.books.append(book_name)
        self.author.append(author_name)
        self.no_of_books += 1
        print(f'"{book_name}" by "{author_name}" has been added to the library.')
   
    def get_no_of_books(self):                                                      # Return number of books in the library
        return self.no_of_books
   
    def print_books(self):                                                          # Print all books in the library
        if self.no_of_books == 0:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book, author in zip(self.books, self.author):
                print(f"- {book} by {author}")

my_library = Library()                                                               # Create a library instance


print("Enter 1 if you want to add a book, otherwise enter any other number.")        # Check if the user wants to add books
i = int(input())

while i == 1:                                                                        # Allow user to add multiple books
    a = input("Enter name of the book: ")
    b = input("Enter name of the author: ")
    my_library.add_book(a, b)
    
    print("Enter 1 to add another book, or any other number to stop.")
    i = int(input())


print("Total number of books:", my_library.get_no_of_books())                        # Print the total number of books and list all books
my_library.print_books()

num1 = input("Are you satisfied? ")                                                  # Ask if the user is satisfied
