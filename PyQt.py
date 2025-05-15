from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
                             QPushButton, QTextEdit, QCheckBox, QInputDialog, QMessageBox)
from PyQt5.QtCore import Qt
from logic import Book, DigitalLibrary, books_by_author

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lib = DigitalLibrary()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 600, 500)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Output text area
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        # Buttons grid
        grid = QGridLayout()
        
        self.add_book_btn = QPushButton("Add Book")
        self.add_ebook_btn = QPushButton("Add eBook")
        self.add_ebook_btn.setEnabled(False)
        self.lend_book_btn = QPushButton("Lend Book")
        self.return_book_btn = QPushButton("Return Book")
        self.available_books_btn = QPushButton("Available Books")
        self.author_books_btn = QPushButton("Books by Author")

        grid.addWidget(self.add_book_btn, 0, 0)
        grid.addWidget(self.add_ebook_btn, 0, 1)
        grid.addWidget(self.lend_book_btn, 1, 0)
        grid.addWidget(self.return_book_btn, 1, 1)
        grid.addWidget(self.available_books_btn, 2, 0)
        grid.addWidget(self.author_books_btn, 2, 1)

        # Checkbox
        self.ebook_checkbox = QCheckBox("Enable Add eBook")
        layout.addLayout(grid)
        layout.addWidget(self.ebook_checkbox)

        # Connect signals
        self.add_book_btn.clicked.connect(self.add_book)
        self.add_ebook_btn.clicked.connect(self.add_ebook)
        self.lend_book_btn.clicked.connect(self.lend_book)
        self.return_book_btn.clicked.connect(self.return_book)
        self.available_books_btn.clicked.connect(self.show_available_books)
        self.author_books_btn.clicked.connect(self.show_books_by_author)
        self.ebook_checkbox.stateChanged.connect(self.toggle_ebook_button)

    def update_output(self, msg):
        self.output.append(msg)

    def toggle_ebook_button(self, state):
        self.add_ebook_btn.setEnabled(state == Qt.Checked)

    def add_book(self):
        title, ok = QInputDialog.getText(self, "Add Book", "Enter book title:")
        if not ok: return
        author, ok = QInputDialog.getText(self, "Add Book", "Enter author:")
        if not ok: return
        isbn, ok = QInputDialog.getText(self, "Add Book", "Enter ISBN:")
        if ok:
            self.lib.add_book(Book(title, author, isbn))
            self.update_output(f"'{title}' added.")

    def add_ebook(self):
        title, ok = QInputDialog.getText(self, "Add eBook", "Enter eBook title:")
        if not ok: return
        author, ok = QInputDialog.getText(self, "Add eBook", "Enter author:")
        if not ok: return
        isbn, ok = QInputDialog.getText(self, "Add eBook", "Enter ISBN:")
        if not ok: return
        size, ok = QInputDialog.getText(self, "Add eBook", "Enter download size (MB):")
        if ok:
            self.lib.add_ebook(title, author, isbn, size)
            self.update_output(f"'{title}' eBook added.")

    def lend_book(self):
        isbn, ok = QInputDialog.getText(self, "Lend Book", "Enter ISBN to lend:")
        if ok:
            result = self.lib.lend_book(isbn)
            self.update_output(result if result else "Book not found or already lent.")

    def return_book(self):
        isbn, ok = QInputDialog.getText(self, "Return Book", "Enter ISBN to return:")
        if ok:
            result = self.lib.return_book(isbn)
            self.update_output(result if result else "Book not found in lent list.")

    def show_available_books(self):
        self.update_output("\nAvailable Books:")
        found = False
        for book in self.lib:
            self.update_output(str(book))
            found = True
        if not found:
            self.update_output("No available books.")

    def show_books_by_author(self):
        author, ok = QInputDialog.getText(self, "Books by Author", "Enter author name:")
        if ok:
            self.update_output(f"\nBooks by '{author}':")
            books = list(books_by_author(self.lib, author))
            if books:
                for book in books:
                    self.update_output(str(book))
            else:
                self.update_output("No books found.")

if __name__ == '__main__':
    app = QApplication([])
    window = LibraryApp()
    window.show()
    app.exec_()