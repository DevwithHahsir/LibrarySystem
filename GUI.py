import tkinter as tk
from tkinter import simpledialog
from logic import Book, DigitalLibrary, books_by_author

lib = DigitalLibrary()

root = tk.Tk()
root.title("Library Management System")
root.geometry("500x400")

# Create a Text widget to display output
output = tk.Text(root, height=15, width=60)
output.pack(pady=10)

# Update the output Text widget
def update_output(msg):
    output.insert(tk.END, msg + "\n")
    output.see(tk.END)

# Function to add a new book
def add_book():
    title = simpledialog.askstring("Input", "Enter book title:")
    author = simpledialog.askstring("Input", "Enter author:")
    isbn = simpledialog.askstring("Input", "Enter ISBN:")
    if title and author and isbn:
        lib.add_book(Book(title, author, isbn))
        update_output(f"'{title}' added.")

# Function to add a new eBook (enabled only when checkbox is checked)
def add_ebook():
    title = simpledialog.askstring("Input", "Enter eBook title:")
    author = simpledialog.askstring("Input", "Enter author:")
    isbn = simpledialog.askstring("Input", "Enter ISBN:")
    size = simpledialog.askstring("Input", "Enter download size (MB):")
    if title and author and isbn and size:
        lib.add_ebook(title, author, isbn, size)
        update_output(f"'{title}' eBook added.")

# Function to lend a book
def lend_book():
    isbn = simpledialog.askstring("Input", "Enter ISBN to lend:")
    if isbn:
        result = lib.lend_book(isbn)
        update_output(result or "Book not found or already lent.")

# Function to return a book
def return_book():
    isbn = simpledialog.askstring("Input", "Enter ISBN to return:")
    if isbn:
        result = lib.return_book(isbn)
        update_output(result or "Book not found in lent list.")

# Function to show available books
def show_available_books():
    update_output("\nAvailable Books:")
    found = False
    for book in lib:
        update_output(str(book))
        found = True
    if not found:
        update_output("No available books.")

# Function to show books by author
def show_books_by_author():
    author = simpledialog.askstring("Input", "Enter author name:")
    update_output(f"\nBooks by '{author}':")
    books = list(books_by_author(lib, author))
    if books:
        for book in books:
            update_output(str(book))
    else:
        update_output("No books found.")

# Function to enable/disable Add eBook button based on checkbox state
def toggle_ebook_button():
    if ebook_checkbox_var.get():
        add_ebook_button.config(state=tk.NORMAL)
    else:
        add_ebook_button.config(state=tk.DISABLED)

# Frame for buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# Add Book Button
tk.Button(btn_frame, text="Add Book", width=15, command=add_book).grid(row=0, column=0, padx=5)

# Add eBook Button (initially disabled)
add_ebook_button = tk.Button(btn_frame, text="Add eBook", width=15, command=add_ebook, state=tk.DISABLED)
add_ebook_button.grid(row=0, column=1, padx=5)

# Lend Book Button
tk.Button(btn_frame, text="Lend Book", width=15, command=lend_book).grid(row=1, column=0, padx=5, pady=5)

# Return Book Button
tk.Button(btn_frame, text="Return Book", width=15, command=return_book).grid(row=1, column=1, padx=5)

# Available Books Button
tk.Button(btn_frame, text="Available Books", width=15, command=show_available_books).grid(row=2, column=0, padx=5)

# Books by Author Button
tk.Button(btn_frame, text="Books by Author", width=15, command=show_books_by_author).grid(row=2, column=1, padx=5)

# Checkbox to enable or disable Add eBook button
ebook_checkbox_var = tk.BooleanVar()
ebook_checkbox = tk.Checkbutton(root, text="Enable Add eBook", variable=ebook_checkbox_var, command=toggle_ebook_button)
ebook_checkbox.pack()

# Run the Tkinter main loop
root.mainloop()
