class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
class Ebook(Book):
    def __init__(self,title,author,file_size ):
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        self.page_count = page_count
class Library:
    books = [Book, EBook, PrintBook]
    def add_book(self, book):
        for b in self.books:
            self.books.append(book)
    def list_books(self):
        print(self.books)