class BookCollection:
    def __init__(self):
        self._books = []  # Внутренний список

    def __getitem__(self, index):
        return self._books[index] # Поддержка индексов и срезов

    def __iter__(self):
        return iter(self._books)

    def __len__(self):
        return len(self._books)

    def add(self, book):
        self._books.append(book) # Добавление книги

    def remove(self, book):
        self._books.remove(book) # Удаление книги

    def __call__(self, author=None, year=None, genre=None):
        """Фильтрация книг по критериям при вызове коллекции как функции"""
        result = []
        for book in self._books:
            if author and book.author != author:
                continue
            if year and book.year != year:
                continue
            if genre and book.genre != genre:
                continue
            result.append(book)
        return result
