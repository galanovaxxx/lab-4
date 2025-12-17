from src.indexdict import IndexDict
from src.bookcollection import BookCollection
from src.errors import DuplicateBookError, EmptyLibraryError


class Library:
    def __init__(self):
        self.books = BookCollection()  # Списковая коллекция
        self.index = IndexDict()  # Словарная коллекция

    def add_book(self, book):
        """Добавить книгу в библиотеку"""
        # Проверка на дубликат
        if book.isbn in self.index:
            raise DuplicateBookError(book.isbn)
        self.books.add(book)
        self.index.add_book(book)

    def remove_book(self, book):
        """Удалить книгу из библиотеки"""
        # Проверка на пустую библиотеку
        if len(self.books) == 0:
            raise EmptyLibraryError()
        self.books.remove(book)
        self.index.remove_book(book)

    def find_by_isbn(self, isbn):
        """Поиск по ISBN"""
        return self.index[isbn]

    def find_by_author(self, author):
        """Поиск по автору"""
        return self.index.get_by_author(author)

    def find_by_year(self, year):
        """Поиск по году"""
        return self.index.get_by_year(year)

    def find_by_genre(self, genre):
        """Поиск по жанру"""
        return self.index.get_by_genre(genre)

    def __len__(self):
        return len(self.books)

    def __contains__(self, isbn):
        return isbn in self.index # проверка наличия книги по ISBN