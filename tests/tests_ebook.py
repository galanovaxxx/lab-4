import pytest
from src.books import EBook
from src.errors import (
    NegativeNumberError,
    NumberTooLargeError,
)


class TestEBook:
    """Тесты для электронной книги"""

    def test_create_valid_ebook(self):
        """Создание электронной книги с валидными данными"""
        book = EBook("Название", "Автор", 2000, "Жанр", "ISBN-001", "PDF", 5.5)
        assert book.file_format == "PDF"
        assert book.file_size_mb == 5.5

    def test_ebook_negative_size_error(self):
        """Ошибка при отрицательном размере файла"""
        with pytest.raises(NegativeNumberError):
            EBook("Название", "Автор", 2000, "Жанр", "ISBN-001", "PDF", -1)

    def test_ebook_zero_size_error(self):
        """Ошибка при нулевом размере файла"""
        with pytest.raises(NegativeNumberError):
            EBook("Название", "Автор", 2000, "Жанр", "ISBN-001", "PDF", 0)

    def test_ebook_too_large_size_error(self):
        """Ошибка при слишком большом размере файла"""
        with pytest.raises(NumberTooLargeError):
            EBook("Название", "Автор", 2000, "Жанр", "ISBN-001", "PDF", 10001)
