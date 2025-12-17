import pytest
from src.books import Book
from src.errors import (
    EmptyStringError,
    ContainsDigitsError,
    LowercaseStartError,
    YearOutOfRangeError,
    ForbiddenSymbolError,
)


class TestBook:
    """Тесты для базового класса Book"""

    def test_create_valid_book(self):
        """Создание книги с валидными данными"""
        book = Book("Война и мир", "Толстой", 1869, "Роман", "ISBN-001")
        assert book.title == "Война и мир"
        assert book.author == "Толстой"
        assert book.year == 1869
        assert book.genre == "Роман"
        assert book.isbn == "ISBN-001"

    def test_book_title_starts_with_digit(self):
        """Название может начинаться с цифры"""
        book = Book("1984", "Оруэлл", 1949, "Антиутопия", "ISBN-002")
        assert book.title == "1984"

    def test_book_empty_title_error(self):
        """Ошибка при пустом названии"""
        with pytest.raises(EmptyStringError):
            Book("", "Автор", 2000, "Жанр", "ISBN-001")

    def test_book_empty_author_error(self):
        """Ошибка при пустом авторе"""
        with pytest.raises(EmptyStringError):
            Book("Название", "", 2000, "Жанр", "ISBN-001")

    def test_book_empty_genre_error(self):
        """Ошибка при пустом жанре"""
        with pytest.raises(EmptyStringError):
            Book("Название", "Автор", 2000, "", "ISBN-001")

    def test_book_author_with_digits_error(self):
        """Ошибка при цифрах в имени автора"""
        with pytest.raises(ContainsDigitsError):
            Book("Название", "Автор123", 2000, "Жанр", "ISBN-001")

    def test_book_genre_with_digits_error(self):
        """Ошибка при цифрах в жанре"""
        with pytest.raises(ContainsDigitsError):
            Book("Название", "Автор", 2000, "Жанр123", "ISBN-001")

    def test_book_title_lowercase_start_error(self):
        """Ошибка при названии с маленькой буквы"""
        with pytest.raises(LowercaseStartError):
            Book("название", "Автор", 2000, "Жанр", "ISBN-001")

    def test_book_author_lowercase_start_error(self):
        """Ошибка при авторе с маленькой буквы"""
        with pytest.raises(LowercaseStartError):
            Book("Название", "автор", 2000, "Жанр", "ISBN-001")

    def test_book_year_too_old_error(self):
        """Ошибка при слишком старом годе"""
        with pytest.raises(YearOutOfRangeError):
            Book("Название", "Автор", 1799, "Жанр", "ISBN-001")

    def test_book_year_too_new_error(self):
        """Ошибка при слишком новом годе"""
        with pytest.raises(YearOutOfRangeError):
            Book("Название", "Автор", 2027, "Жанр", "ISBN-001")

    def test_book_forbidden_symbol_in_title(self):
        """Ошибка при запрещённом символе в названии"""
        with pytest.raises(ForbiddenSymbolError):
            Book("Название@книги", "Автор", 2000, "Жанр", "ISBN-001")

    def test_book_forbidden_symbol_in_author(self):
        """Ошибка при запрещённом символе в авторе"""
        with pytest.raises(ForbiddenSymbolError):
            Book("Название", "Автор#Имя", 2000, "Жанр", "ISBN-001")

    def test_book_equality_by_isbn(self):
        """Книги равны по ISBN"""
        book1 = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        book2 = Book("Другое", "Другой", 2010, "Другой", "ISBN-001")
        assert book1 == book2

    def test_book_repr(self):
        """Строковое представление книги"""
        book = Book("Война и мир", "Толстой", 1869, "Роман", "ISBN-001")
        assert "Война и мир" in repr(book)
        assert "Толстой" in repr(book)