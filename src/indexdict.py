class IndexDict:
    def __init__(self):
        self._by_isbn = {}
        self._by_author = {}
        self._by_year = {}
        self._by_genre = {}

    def __getitem__(self, key):
        # Доступ по ключу (ISBN)
        return self._by_isbn.get(key)

    def __iter__(self):
        return iter(self._by_isbn)

    def __len__(self):
        return len(self._by_isbn)

    def __contains__(self, key):
        return key in self._by_isbn

    def add_book(self, book):
        """Добавить книгу в индексы"""
        self._by_isbn[book.isbn] = book

        # По автору (список книг)
        if book.author not in self._by_author:
            self._by_author[book.author] = []
        self._by_author[book.author].append(book)

        # По году (список книг)
        if book.year not in self._by_year:
            self._by_year[book.year] = []
        self._by_year[book.year].append(book)

        # По жанру (список книг)
        if book.genre not in self._by_genre:
            self._by_genre[book.genre] = []
        self._by_genre[book.genre].append(book)

    def remove_book(self, book):
        """Удалить книгу из индексов"""
        if book.isbn not in self._by_isbn:
            raise KeyError(f"Книга с ISBN '{book.isbn}' не найдена")
        del self._by_isbn[book.isbn]
        self._by_author[book.author].remove(book)
        self._by_year[book.year].remove(book)
        self._by_genre[book.genre].remove(book)

    def get_by_author(self, author):
        """Получить книги по автору"""
        if author not in self._by_author:
            raise KeyError(f"Автор '{author}' не найден")
        return self._by_author[author]

    def get_by_year(self, year):
        """Получить книги по году"""
        if year not in self._by_year:
            raise KeyError(f"Книги {year} года не найдены")
        return self._by_year[year]

    def get_by_genre(self, genre):
        """Получить книги по жанру"""
        if genre not in self._by_genre:
            raise KeyError(f"Жанр '{genre}' не найден")
        return self._by_genre[genre]
