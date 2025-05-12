class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []
        self.lent = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book.title}' removed")

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book not in self.lent:
                self.lent.append(book)
                print(f"'{book.title}' lended kar di gayi hai")
                return
        print("Book not found or already lended")

    def return_book(self, isbn):
        for book in self.lent:
            if book.isbn == isbn:
                self.lent.remove(book)
                print(f"'{book.title}' wapas le li gayi hai")
                return
        print("Book not found in lent list")

    def __iter__(self):
        return (book for book in self.books if book not in self.lent)


def books_by_author(library, author):
    for book in library.books:
        if book.author.lower() == author.lower():
            yield book


class Ebook(Book):
    def __init__(self, title, author, isbn, download_size):
        super().__init__(title, author, isbn)
        self.download_size = download_size

    def __str__(self):
        return f"{self.title} by {self.author} (eBook, {self.download_size}MB, ISBN: {self.isbn})"


class DigitalLibrary(Library):
    def __init__(self):
        super().__init__()
        self.ebooks = []

    def add_ebook(self, title, author, isbn, download_size):
        ebook = Ebook(title, author, isbn, download_size)
        self.books.append(ebook)
        self.ebooks.append(ebook)
        print(f"eBook '{ebook.title}' add kar di gayi hai ({ebook.download_size}MB)")


# --------------------- MAIN INTERFACE ---------------------

lib = DigitalLibrary()

while True:
        print("\n📚 Library Menu:")
        print("1. Add Book")
        print("2. Add eBook")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Show Available Books")
        print("6. Show Books by Author")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            lib.add_book(Book(title, author, isbn))

        elif choice == '2':
            title = input("Enter eBook title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            size = input("Enter download size (MB): ")
            lib.add_ebook(title, author, isbn, size)

        elif choice == '3':
            isbn = input("Enter ISBN to lend: ")
            lib.lend_book(isbn)

        elif choice == '4':
            isbn = input("Enter ISBN to return: ")
            lib.return_book(isbn)

        elif choice == '5':
            print("\n✅ Available Books:")
            for book in lib:
                print(book)

        elif choice == '6':
            author = input("Enter author name: ")
            found = False
            print(f"\n📖 Books by '{author}':")
            for book in books_by_author(lib, author):
                print(book)
                found = True
            if not found:
                print("No books found for that author.")

        elif choice == '7':
            print("Exiting... 📕")
            break
        else:
            print("Invalid option. Try again.")


# Run the program

