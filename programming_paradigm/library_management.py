class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title               
        self.author = author            
        self._is_checked_out = False    

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it’s available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out or not found.")

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")