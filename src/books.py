from src.errors import (
    NegativeNumberError,
    NumberTooLargeError,
    InvalidCoverTypeError,
    EmptyStringError,
    ContainsDigitsError,
    LowercaseStartError,
    ForbiddenSymbolError,
    YearOutOfRangeError,
)

class Book:
    def __init__(self, title, author, year, genre, isbn):
        # Валидация названия
        if title == "" or title is None or title.strip() == "":
            raise EmptyStringError("название")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in title:
                raise ForbiddenSymbolError("название", title)
        first_char = title.strip()[0]
        if first_char.isupper() == False and first_char.isdigit() == False:
            raise LowercaseStartError("название", title)

        # Валидация автора
        if author == "" or author is None or author.strip() == "":
            raise EmptyStringError("автор")
        for char in author:
            if char.isdigit():
                raise ContainsDigitsError("автор", author)
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in author:
                raise ForbiddenSymbolError("автор", author)
        if author.strip()[0].isupper() == False:
            raise LowercaseStartError("автор", author)

        # Валидация года
        if year < 1800 or year > 2026:
            raise YearOutOfRangeError(year, 1800, 2026)

        # Валидация жанра
        if genre == "" or genre is None or genre.strip() == "":
            raise EmptyStringError("жанр")
        for char in genre:
            if char.isdigit():
                raise ContainsDigitsError("жанр", genre)
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in genre:
                raise ForbiddenSymbolError("жанр", genre)

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.title}' {self.author}, год издания: {self.year}, жанр: {str(self.genre)}, isbn: {self.isbn}"

    def __eq__(self, other):
        return self.isbn == other.isbn


class PrintedBook(Book):
    """Печатная книга"""

    def __init__(self, title, author, year, genre, isbn, pages, cover_type="мягкая"):
        super().__init__(title, author, year, genre, isbn)

        # Валидация страниц
        if pages <= 0:
            raise NegativeNumberError("страницы", pages)
        if pages > 10000:
            raise NumberTooLargeError("страницы", pages, 10000)

        # Валидация типа обложки
        if cover_type != "мягкая" and cover_type != "твёрдая":
            raise InvalidCoverTypeError(cover_type)

        self.pages = pages
        self.cover_type = cover_type

    def __repr__(self):
        return f"Печатная книга : '{self.title}', {self.author}, год издания: {self.year}, жанр: {self.genre}, isbn: {self.isbn}, {self.pages} стр., {self.cover_type} обложка"


class EBook(Book):
    """Электронная книга"""

    def __init__(self, title, author, year, genre, isbn, file_format, file_size_mb):
        super().__init__(title, author, year, genre, isbn)

        # Валидация размера файла
        if file_size_mb <= 0:
            raise NegativeNumberError("размер файла", file_size_mb)
        if file_size_mb > 10000:
            raise NumberTooLargeError("размер файла", file_size_mb, 10000)

        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def __repr__(self):
        return f"Электронная книга: '{self.title}', {self.author}, год издания: {self.year}, жанр: {self.genre}, isbn: {self.isbn}, формат: {self.file_format}, {self.file_size_mb} МБ"


class AudioBook(Book):
    """Аудиокнига"""

    def __init__(self, title, author, year, genre, isbn, duration_minutes, narrator):
        super().__init__(title, author, year, genre, isbn)

        # Валидация длительности
        if duration_minutes <= 0:
            raise NegativeNumberError("длительность", duration_minutes)
        if duration_minutes > 10000:
            raise NumberTooLargeError("длительность", duration_minutes, 10000)

        # Валидация диктора
        if narrator == "" or narrator is None or narrator.strip() == "":
            raise EmptyStringError("диктор")
        for char in narrator:
            if char.isdigit():
                raise ContainsDigitsError("диктор", narrator)
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in narrator:
                raise ForbiddenSymbolError("диктор", narrator)
        if narrator.strip()[0].isupper() == False:
            raise LowercaseStartError("диктор", narrator)

        self.duration_minutes = duration_minutes
        self.narrator = narrator

    def __repr__(self):
        return f"Аудиокнига: '{self.title}', {self.author}, год записи: {self.year}, жанр: {self.genre}, isbn: {self.isbn}, {self.duration_minutes} мин., читает: {self.narrator}"


