import random
from src.books import Book
from src.library import Library


# Данные для генерации случайных книг
TITLES = ["Война и мир", "1984", "Мастер и Маргарита", "Преступление и наказание", "Гарри Поттер"]
AUTHORS = ["Толстой", "Оруэлл", "Булгаков", "Достоевский", "Роулинг"]
GENRES = ["Роман", "Антиутопия", "Фантастика", "Детектив", "Учебник"]


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """Запуск симуляции библиотеки"""

    # 1. Установка seed для воспроизводимости
    if seed is not None:
        random.seed(seed)

    # 2. Создание библиотеки
    library = Library()

    # 3. Добавление начальных книг
    for i in range(3):
        book = Book(
            title=random.choice(TITLES),
            author=random.choice(AUTHORS),
            year=random.randint(1900, 2024),
            genre=random.choice(GENRES),
            isbn=f"ISBN-{i}"
        )
        library.add_book(book)
        print(f"[Начало] Добавлена книга: {book}")

    print(f"\n{'=' * 50}")
    print(f"Начало симуляции: {steps} шагов")
    print(f"{'=' * 50}\n")

    # 4. Список возможных событий
    events = ["add_book", "remove_book", "search_by_author", "search_by_genre", "get_nonexistent"]

    # 5. Основной цикл симуляции
    for step in range(1, steps + 1):
        event = random.choice(events)
        print(f"Шаг {step}. Событие: {event}")

        if event == "add_book":
            # Добавление новой книги
            isbn = f"ISBN-{random.randint(100, 999)}"
            book = Book(
                title=random.choice(TITLES),
                author=random.choice(AUTHORS),
                year=random.randint(1900, 2025),
                genre=random.choice(GENRES),
                isbn=isbn
            )
            library.add_book(book)
            print(f"Добавлена: {book}")

        elif event == "remove_book":
            # Удаление случайной книги
            if len(library) > 0:
                book = random.choice(list(library.books))
                library.remove_book(book)
                print(f"Удалена: {book}")
            else:
                print(f"Библиотека пуста, нечего удалять")

        elif event == "search_by_author":
            # Поиск по автору
            author = random.choice(AUTHORS)
            results = library.find_by_author(author)
            print(f"Поиск по автору '{author}': найдено {len(results)} книг")

        elif event == "search_by_genre":
            # Поиск по жанру
            genre = random.choice(GENRES)
            results = library.find_by_genre(genre)
            print(f"Поиск по жанру '{genre}': найдено {len(results)} книг")

        elif event == "get_nonexistent":
            # Попытка получить несуществующую книгу
            fake_isbn = "ISBN-NOT-EXISTS"
            result = library.find_by_isbn(fake_isbn)
            if result is None:
                print(f"Книга с ISBN '{fake_isbn}' не найдена (ожидаемо)")
            else:
                print(f"Неожиданно найдена: {result}")

    print(f"Симуляция завершена. Книг в библиотеке: {len(library)}")

if __name__ == "__main__":
    run_simulation(steps=20, seed=42)