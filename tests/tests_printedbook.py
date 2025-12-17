import pytest
from src.books import PrintedBook
from src.errors import (
    NegativeNumberError,
    NumberTooLargeError,
    InvalidCoverTypeError,
)


class TestPrintedBook:
    """Тесты для печатной книги"""

    def test_create_valid_printed_book(self):
        """Создание печатной книги с валидными данными"""
        book = PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 300, "мягкая")
        assert book.pages == 300
        assert book.cover_type == "мягкая"

    def test_printed_book_hard_cover(self):
        """Печатная книга с твёрдой обложкой"""
        book = PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 300, "твёрдая")
        assert book.cover_type == "твёрдая"

    def test_printed_book_negative_pages_error(self):
        """Ошибка при отрицательном количестве страниц"""
        with pytest.raises(NegativeNumberError):
            PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", -10, "мягкая")

    def test_printed_book_zero_pages_error(self):
        """Ошибка при нулевом количестве страниц"""
        with pytest.raises(NegativeNumberError):
            PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 0, "мягкая")

    def test_printed_book_too_many_pages_error(self):
        """Ошибка при слишком большом количестве страниц"""
        with pytest.raises(NumberTooLargeError):
            PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 10001, "мягкая")

    def test_printed_book_invalid_cover_error(self):
        """Ошибка при неверном типе обложки"""
        with pytest.raises(InvalidCoverTypeError):
            PrintedBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 300, "картонная")

