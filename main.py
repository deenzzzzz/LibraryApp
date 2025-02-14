import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, book_id, title, author, genre, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.copies_available = copies_available

    def borrow(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False

    def return_book(self):
        self.copies_available += 1

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.library = Library("Sunny Library")

        # Add sample books and members
        self.library.add_book(Book(1, "The Little Prince", "Antoine de Saint-Exupéry", "Fiction", 3))
        self.library.add_book(Book(2, "Anne of Green Gables", "L. M. Montgomery", "Classic", 2))
        self.library.add_member(Member(101, "Alice Brown"))
        self.library.add_member(Member(102, "Charlie Green"))

        self.master.title("Library Management System")
        self.master.geometry("500x400")
        self.master.configure(bg="#f4f4f4")

        self.label = tk.Label(master, text="📚 Library Management System", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333333")
        self.label.pack(pady=10)

        self.book_entry = tk.Entry(master, font=("Arial", 12), width=30, fg="#888888")
        self.book_entry.pack(pady=5)
        self.book_entry.insert(0, "Enter book title")
        self.book_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.book_entry, "Enter book title"))
        self.book_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.book_entry, "Enter book title"))

        self.member_entry = tk.Entry(master, font=("Arial", 12), width=30, fg="#888888")
        self.member_entry.pack(pady=5)
        self.member_entry.insert(0, "Enter member name")
        self.member_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.member_entry, "Enter member name"))
        self.member_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.member_entry, "Enter member name"))

        self.borrow_button = tk.Button(master, text="Borrow Book", command=self.borrow_book, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.borrow_button.pack(pady=5)

        self.return_button = tk.Button(master, text="Return Book", command=self.return_book, font=("Arial", 12), bg="#FF9800", fg="white", padx=10, pady=5)
        self.return_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="#f4f4f4", fg="#333333")
        self.result_label.pack(pady=5)

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#000000")

    def restore_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="#888888")

    def borrow_book(self):
        book_title = self.book_entry.get()
        member_name = self.member_entry.get()
        book = self.library.find_book(book_title)
        member = self.library.find_member(member_name)

        if book and member:
            if member.borrow_book(book):
                messagebox.showinfo("Success", f"{member_name} borrowed {book_title}")
            else:
                messagebox.showerror("Error", "Book not available")
        else:
            messagebox.showerror("Error", "Book or member not found")

    def return_book(self):
        book_title = self.book_entry.get()
        member_name = self.member_entry.get()
        book = self.library.find_book(book_title)
        member = self.library.find_member(member_name)

        if book and member:
            if member.return_book(book):
                messagebox.showinfo("Success", f"{member_name} returned {book_title}")
            else:
                messagebox.showerror("Error", "Member does not have this book")
        else:
            messagebox.showerror("Error", "Book or member not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
