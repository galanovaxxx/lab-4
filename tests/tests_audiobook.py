import pytest
from src.books import AudioBook
from src.errors import (
    EmptyStringError,
    ContainsDigitsError,
    LowercaseStartError,
    NegativeNumberError,
    NumberTooLargeError,
)


class TestAudioBook:
    """Тесты для аудиокниги"""

    def test_create_valid_audiobook(self):
        """Создание аудиокниги с валидными данными"""
        book = AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 180, "Диктор")
        assert book.duration_minutes == 180
        assert book.narrator == "Диктор"

    def test_audiobook_negative_duration_error(self):
        """Ошибка при отрицательной длительности"""
        with pytest.raises(NegativeNumberError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", -10, "Диктор")

    def test_audiobook_zero_duration_error(self):
        """Ошибка при нулевой длительности"""
        with pytest.raises(NegativeNumberError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 0, "Диктор")

    def test_audiobook_too_long_duration_error(self):
        """Ошибка при слишком большой длительности"""
        with pytest.raises(NumberTooLargeError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 10001, "Диктор")

    def test_audiobook_empty_narrator_error(self):
        """Ошибка при пустом дикторе"""
        with pytest.raises(EmptyStringError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 180, "")

    def test_audiobook_narrator_with_digits_error(self):
        """Ошибка при цифрах в имени диктора"""
        with pytest.raises(ContainsDigitsError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 180, "Диктор123")

    def test_audiobook_narrator_lowercase_error(self):
        """Ошибка при дикторе с маленькой буквы"""
        with pytest.raises(LowercaseStartError):
            AudioBook("Название", "Автор", 2000, "Жанр", "ISBN-001", 180, "диктор")
