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

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book not in self.lent:
                self.lent.append(book)
                return f"'{book.title}' lended kar di gayi hai"
        return "Book not found or already lended"

    def return_book(self, isbn):
        for book in self.lent:
            if book.isbn == isbn:
                self.lent.remove(book)
                return f"'{book.title}' wapas le li gayi hai"
        return "Book not found in lent list"

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
