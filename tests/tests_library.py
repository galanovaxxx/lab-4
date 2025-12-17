import pytest
from src.books import Book
from src.books import PrintedBook, EBook, AudioBook
from src.library import Library
from src.errors import (
    DuplicateBookError,
    EmptyLibraryError
)


class TestLibrary:
    """Тесты для библиотеки"""

    def test_empty_library(self):
        """Пустая библиотека"""
        library = Library()
        assert len(library) == 0

    def test_add_book_to_library(self):
        """Добавление книги в библиотеку"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        assert len(library) == 1

    def test_add_duplicate_book_error(self):
        """Ошибка при добавлении дубликата"""
        library = Library()
        book1 = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        book2 = Book("Другое", "Другой", 2010, "Другой", "ISBN-001")
        library.add_book(book1)
        with pytest.raises(DuplicateBookError):
            library.add_book(book2)

    def test_remove_book_from_library(self):
        """Удаление книги из библиотеки"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        library.remove_book(book)
        assert len(library) == 0

    def test_remove_book_from_empty_library_error(self):
        """Ошибка при удалении из пустой библиотеки"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        with pytest.raises(EmptyLibraryError):
            library.remove_book(book)

    def test_find_by_isbn(self):
        """Поиск по ISBN"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        found = library.find_by_isbn("ISBN-001")
        assert found == book

    def test_find_by_isbn_not_found(self):
        """Поиск по несуществующему ISBN возвращает None"""
        library = Library()
        found = library.find_by_isbn("NONEXISTENT")
        assert found is None

    def test_find_by_author(self):
        """Поиск по автору"""
        library = Library()
        book = Book("Название", "Толстой", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        result = library.find_by_author("Толстой")
        assert len(result) == 1

    def test_find_by_author_not_found_error(self):
        """Ошибка при поиске несуществующего автора"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        with pytest.raises(KeyError):
            library.find_by_author("Неизвестный")

    def test_find_by_year(self):
        """Поиск по году"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        result = library.find_by_year(2000)
        assert len(result) == 1

    def test_find_by_genre(self):
        """Поиск по жанру"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Роман", "ISBN-001")
        library.add_book(book)
        result = library.find_by_genre("Роман")
        assert len(result) == 1

    def test_contains_isbn(self):
        """Проверка наличия ISBN в библиотеке"""
        library = Library()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        library.add_book(book)
        assert "ISBN-001" in library
        assert "ISBN-999" not in library

    def test_library_with_different_book_types(self):
        """Библиотека с разными типами книг"""
        library = Library()
        book = Book("Книга", "Автор", 2000, "Жанр", "ISBN-001")
        printed = PrintedBook("Печатная", "Автор", 2001, "Жанр", "ISBN-002", 300, "мягкая")
        ebook = EBook("Электронная", "Автор", 2002, "Жанр", "ISBN-003", "PDF", 5.0)
        audio = AudioBook("Аудио", "Автор", 2003, "Жанр", "ISBN-004", 180, "Диктор")

        library.add_book(book)
        library.add_book(printed)
        library.add_book(ebook)
        library.add_book(audio)

        assert len(library) == 4
