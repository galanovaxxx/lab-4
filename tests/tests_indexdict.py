import pytest
from src.books import Book
from src.indexdict import IndexDict


class TestIndexDict:
    """Тесты для индексного словаря"""

    def test_empty_index(self):
        """Пустой индекс"""
        index = IndexDict()
        assert len(index) == 0

    def test_add_book_to_index(self):
        """Добавление книги в индекс"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        assert len(index) == 1
        assert "ISBN-001" in index

    def test_getitem_by_isbn(self):
        """Доступ по ISBN через __getitem__"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        assert index["ISBN-001"] == book

    def test_getitem_nonexistent_isbn(self):
        """Доступ по несуществующему ISBN возвращает None"""
        index = IndexDict()
        assert index["NONEXISTENT"] is None

    def test_contains_isbn(self):
        """Проверка наличия ISBN через __contains__"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        assert "ISBN-001" in index
        assert "ISBN-999" not in index

    def test_get_by_author(self):
        """Получение книг по автору"""
        index = IndexDict()
        book1 = Book("Книга1", "Толстой", 2000, "Роман", "ISBN-001")
        book2 = Book("Книга2", "Толстой", 2001, "Повесть", "ISBN-002")
        index.add_book(book1)
        index.add_book(book2)
        result = index.get_by_author("Толстой")
        assert len(result) == 2

    def test_get_by_author_not_found_error(self):
        """Ошибка при поиске несуществующего автора"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        with pytest.raises(KeyError):
            index.get_by_author("Неизвестный")

    def test_get_by_year(self):
        """Получение книг по году"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        result = index.get_by_year(2000)
        assert len(result) == 1

    def test_get_by_year_not_found_error(self):
        """Ошибка при поиске несуществующего года"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        with pytest.raises(KeyError):
            index.get_by_year(1999)

    def test_get_by_genre(self):
        """Получение книг по жанру"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Роман", "ISBN-001")
        index.add_book(book)
        result = index.get_by_genre("Роман")
        assert len(result) == 1

    def test_get_by_genre_not_found_error(self):
        """Ошибка при поиске несуществующего жанра"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Роман", "ISBN-001")
        index.add_book(book)
        with pytest.raises(KeyError):
            index.get_by_genre("Фантастика")

    def test_remove_book_from_index(self):
        """Удаление книги из индекса"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        index.add_book(book)
        index.remove_book(book)
        assert len(index) == 0
        assert "ISBN-001" not in index

    def test_remove_nonexistent_book_error(self):
        """Ошибка при удалении несуществующей книги"""
        index = IndexDict()
        book = Book("Название", "Автор", 2000, "Жанр", "ISBN-001")
        with pytest.raises(KeyError):
            index.remove_book(book)
