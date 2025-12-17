import pytest
from src.books import Book
from src.bookcollection import BookCollection


class TestBookCollection:
    """Тесты для коллекции книг (на основе списка)"""

    def test_empty_collection(self):
        """Пустая коллекция"""
        collection = BookCollection()
        assert len(collection) == 0

    def test_add_book_to_collection(self):
        """Добавление книги в коллекцию"""
        collection = BookCollection()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        collection.add(book)
        assert len(collection) == 1

    def test_remove_book_from_collection(self):
        """Удаление книги из коллекции"""
        collection = BookCollection()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        collection.add(book)
        collection.remove(book)
        assert len(collection) == 0

    def test_getitem_by_index(self):
        """Доступ по индексу"""
        collection = BookCollection()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        collection.add(book)
        assert collection[0] == book

    def test_iterate_collection(self):
        """Итерация по коллекции"""
        collection = BookCollection()
        book1 = Book("Книга1", "Автор", 2000, "Жанр", "ISBN-001")
        book2 = Book("Книга2", "Автор", 2001, "Жанр", "ISBN-002")
        collection.add(book1)
        collection.add(book2)
        books = list(collection)
        assert len(books) == 2

    def test_call_filter_by_author(self):
        """Фильтрация по автору через __call__"""
        collection = BookCollection()
        book1 = Book("Книга1", "Толстой", 2000, "Роман", "ISBN-001")
        book2 = Book("Книга2", "Пушкин", 2001, "Поэзия", "ISBN-002")
        book3 = Book("Книга3", "Толстой", 2002, "Повесть", "ISBN-003")
        collection.add(book1)
        collection.add(book2)
        collection.add(book3)
        result = collection(author="Толстой")
        assert len(result) == 2

    def test_call_filter_by_year(self):
        """Фильтрация по году через __call__"""
        collection = BookCollection()
        book1 = Book("Книга1", "Автор", 2000, "Жанр", "ISBN-001")
        book2 = Book("Книга2", "Автор", 2001, "Жанр", "ISBN-002")
        collection.add(book1)
        collection.add(book2)
        result = collection(year=2000)
        assert len(result) == 1

    def test_call_filter_by_genre(self):
        """Фильтрация по жанру через __call__"""
        collection = BookCollection()
        book1 = Book("Книга1", "Автор", 2000, "Роман", "ISBN-001")
        book2 = Book("Книга2", "Автор", 2001, "Поэзия", "ISBN-002")
        collection.add(book1)
        collection.add(book2)
        result = collection(genre="Роман")
        assert len(result) == 1

    def test_call_filter_multiple_criteria(self):
        """Фильтрация по нескольким критериям через __call__"""
        collection = BookCollection()
        book1 = Book("Книга1", "Толстой", 2000, "Роман", "ISBN-001")
        book2 = Book("Книга2", "Толстой", 2001, "Роман", "ISBN-002")
        book3 = Book("Книга3", "Пушкин", 2000, "Роман", "ISBN-003")
        collection.add(book1)
        collection.add(book2)
        collection.add(book3)
        result = collection(author="Толстой", genre="Роман")
        assert len(result) == 2
