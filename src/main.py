import random
from src.books import PrintedBook, EBook, AudioBook
from src.library import Library
from src.constants import TITLES, AUTHORS, GENRES, NARRATORS, FILE_FORMATS, COVER_TYPES
from src.simulation import run_simulation


# Константа с запрещёнными символами (set для быстрой проверки)
FORBIDDEN_SYMBOLS = set('@#$%^&*=+<>/\\|~`')


def has_forbidden(text: str) -> bool:
    """Проверяет, содержит ли текст запрещённые символы"""
    return any(char in FORBIDDEN_SYMBOLS for char in text)


def has_digits(text: str) -> bool:
    """Проверяет, содержит ли текст цифры"""
    return any(char.isdigit() for char in text)


def print_menu():
    """Вывод главного меню"""
    print("СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
    print("")
    print("1. Добавить книгу")
    print("2. Взять книгу (удалить)")
    print("3. Найти книгу по ISBN")
    print("4. Найти книги по автору")
    print("5. Найти книги по жанру")
    print("6. Найти книги по году")
    print("7. Показать все книги")
    print("8. Запустить симуляцию")
    print("0. Выход")


def print_book_type_menu():
    """Меню выбора типа книги"""
    print("\nВыберите тип книги:")
    print("1. Печатная книга")
    print("2. Электронная книга")
    print("3. Аудиокнига")


def input_title() -> str:
    """Ввод названия с валидацией"""
    print(f"\nВведите название книги:")
    print(f"Предложенные варианты: {', '.join(TITLES)}")
    while True:
        title = input("Ваш ввод: ").strip()
        if title == "":
            print("Ошибка: название не может быть пустым")
            continue
        if has_forbidden(title):
            print("Ошибка: название содержит запрещённый символ")
            continue
        first_char = title[0]
        if not first_char.isupper() and not first_char.isdigit():
            print("Ошибка: название должно начинаться с большой буквы или цифры")
            continue
        return title


def input_author() -> str:
    """Ввод автора с валидацией"""
    print(f"\nВведите автора:")
    print(f"Предложенные варианты: {', '.join(AUTHORS)}")
    while True:
        author = input("Ваш ввод: ").strip()
        if author == "":
            print("Ошибка: имя автора не может быть пустым")
            continue
        if has_digits(author):
            print("Ошибка: имя автора не должно содержать цифры")
            continue
        if has_forbidden(author):
            print("Ошибка: имя автора содержит запрещённый символ")
            continue
        if not author[0].isupper():
            print("Ошибка: имя автора должно начинаться с большой буквы")
            continue
        return author


def input_year() -> int:
    """Ввод года с валидацией"""
    while True:
        year_str = input("Введите год издания: ").strip()
        if year_str.lstrip('-').isdigit() == False:
            print("Ошибка: введите число")
            continue
        year = int(year_str)
        if year < 1800:
            print(f"Ошибка: слишком маленький год")
            continue
        if year > 2026:
            print(f"Ошибка: слишком большой год")
            continue
        return year


def input_genre() -> str:
    """Ввод жанра с валидацией"""
    print(f"\nВведите жанр:")
    print(f"Предложенные варианты: {', '.join(GENRES)}")
    while True:
        genre = input("Ваш ввод: ").strip()
        if genre == "":
            print("Ошибка: жанр не может быть пустым")
            continue
        if has_digits(genre):
            print("Ошибка: жанр не должен содержать цифры")
            continue
        if has_forbidden(genre):
            print("Ошибка: жанр содержит запрещённый символ")
            continue
        return genre


def input_pages() -> int:
    """Ввод количества страниц с валидацией"""
    while True:
        pages_str = input("Введите количество страниц: ").strip()
        if pages_str.isdigit() == False:
            print("Ошибка: введите положительное число")
            continue
        pages = int(pages_str)
        if pages <= 0:
            print("Ошибка: количество страниц должно быть положительным")
            continue
        if pages > 10000:
            print("Ошибка: слишком большое количество страниц (максимум 10000)")
            continue
        return pages


def input_cover_type() -> str:
    """Ввод типа обложки с валидацией"""
    print(f"\nВведите тип обложки:")
    print(f"Предложенные варианты: {', '.join(COVER_TYPES)}")
    while True:
        cover = input("Ваш ввод: ").strip()
        if cover != "мягкая" and cover != "твёрдая":
            print("Ошибка: тип обложки должен быть 'мягкая' или 'твёрдая'")
            continue
        return cover


def input_file_size() -> float:
    """Ввод размера файла с валидацией"""
    while True:
        size_str = input("Введите размер файла (МБ): ").strip()
        try:
            size = float(size_str)
        except ValueError:
            print("Ошибка: введите число")
            continue
        if size <= 0:
            print("Ошибка: размер файла должен быть положительным")
            continue
        if size > 10000:
            print("Ошибка: слишком большой размер файла (максимум 10000 МБ)")
            continue
        return size


def input_duration() -> float:
    """Ввод длительности с валидацией"""
    while True:
        dur_str = input("Введите длительность (в минутах): ").strip()
        try:
            duration = float(dur_str)
        except ValueError:
            print("Ошибка: введите число")
            continue
        if duration <= 0:
            print("Ошибка: длительность должна быть положительной")
            continue
        if duration > 10000:
            print("Ошибка: слишком большая длительность (максимум 10000 минут)")
            continue
        return duration


def input_narrator() -> str:
    """Ввод диктора с валидацией"""
    print(f"\nВведите имя диктора:")
    print(f"Предложенные варианты: {', '.join(NARRATORS)}")
    while True:
        narrator = input("Ваш ввод: ").strip()
        if narrator == "":
            print("Ошибка: имя диктора не может быть пустым")
            continue
        if has_digits(narrator):
            print("Ошибка: имя диктора не должно содержать цифры")
            continue
        if has_forbidden(narrator):
            print("Ошибка: имя диктора содержит запрещённый символ")
            continue
        if not narrator[0].isupper():
            print("Ошибка: имя диктора должно начинаться с большой буквы")
            continue
        return narrator


def add_book(library: Library) -> None:
    """Добавление книги в библиотеку"""
    print_book_type_menu()
    book_type = input("Выберите тип (1-3): ").strip()

    title = input_title()
    author = input_author()
    year = input_year()
    genre = input_genre()
    isbn = input("Введите ISBN: ").strip()

    # Проверка дубликата ISBN
    if isbn in library.index:
        print(f"Ошибка: книга с ISBN '{isbn}' уже существует в библиотеке")
        return

    elif book_type == "1":
        pages = input_pages()
        cover = input_cover_type()
        book = PrintedBook(title, author, year, genre, isbn, pages, cover)

    elif book_type == "2":
        print(f"\nВведите формат файла:")
        print(f"Предложенные варианты: {', '.join(FILE_FORMATS)}")
        file_format = input("Ваш ввод: ").strip()
        file_size = input_file_size()
        book = EBook(title, author, year, genre, isbn, file_format, file_size)

    elif book_type == "3":
        duration = input_duration()
        narrator = input_narrator()
        book = AudioBook(title, author, year, genre, isbn, duration, narrator)

    else:
        print("Неверный выбор типа книги!")
        return

    library.add_book(book)
    print(f"Книга добавлена: {book}")


def take_book(library: Library) -> None:
    """Взять книгу из библиотеки (удалить)"""
    if len(library) == 0:
        print("Ошибка: библиотека пуста")
        return

    print("\nКниги в библиотеке:")
    for i, book in enumerate(library.books, 1):
        print(f"{i}. {book})")

    isbn = input("\nВведите ISBN книги, которую хотите взять: ").strip()
    book = library.find_by_isbn(isbn)

    if book is None:
        print(f"Книга с ISBN '{isbn}' не найдена!")
    else:
        library.remove_book(book)
        print(f"Вы взяли книгу: {book}")


def find_by_isbn(library: Library) -> None:
    """Поиск книги по ISBN"""
    isbn = input("Введите ISBN: ").strip()
    book = library.find_by_isbn(isbn)

    if book is None:
        print(f"Книга с ISBN '{isbn}' не найдена!")
    else:
        print(f"Найдена книга: {book}")
        print(f"Автор: {book.author}")
        print(f"Год: {book.year}")
        print(f"Жанр: {book.genre}")


def find_by_author(library: Library) -> None:
    """Поиск книг по автору"""
    # Показываем доступных авторов
    available_authors = set()
    for book in library.books:
        available_authors.add(book.author)

    if not available_authors:
        print("Библиотека пуста!")
        return

    print(f"\nАвторы в библиотеке: {', '.join(available_authors)}")
    author = input("Введите имя автора: ").strip()

    try:
        results = library.find_by_author(author)
        print(f"Найдено книг: {len(results)}")
        for book in results:
            print(f"{book}")
    except KeyError as e:
        print(f"Ошибка: {e}")


def find_by_genre(library: Library) -> None:
    """Поиск книг по жанру"""
    # Показываем доступные жанры
    available_genres = set()
    for book in library.books:
        available_genres.add(book.genre)

    if not available_genres:
        print("Библиотека пуста!")
        return

    print(f"\nЖанры в библиотеке: {', '.join(available_genres)}")
    genre = input("Введите жанр: ").strip()

    try:
        results = library.find_by_genre(genre)
        print(f"Найдено книг: {len(results)}")
        for book in results:
            print(f"{book}")
    except KeyError as e:
        print(f"Ошибка: {e}")


def find_by_year(library: Library) -> None:
    """Поиск книг по году"""
    while True:
        try:
            year = int(input("Введите год: ").strip())
            break
        except ValueError:
            print("Ошибка: введите число!")

    try:
        results = library.find_by_year(year)
        print(f"Найдено книг: {len(results)}")
        for book in results:
            print(f"{book}")
    except KeyError as e:
        print(f"Ошибка: {e}")


def show_all_books(library: Library) -> None:
    """Показать все книги в библиотеке"""
    if len(library) == 0:
        print("Библиотека пуста!")
        return

    print(f"\nВсего книг в библиотеке: {len(library)}")

    for i, book in enumerate(library.books, 1):
        print(f"{i}. {book}")

def main() -> None:
    """Точка входа в приложение"""
    library = Library()

    # Добавляем несколько начальных книг для демонстрации
    initial_books = [
        PrintedBook("Война и мир", "Толстой", 1869, "Роман", "ISBN-001", 1225, "твёрдая"),
        PrintedBook("1984", "Оруэлл", 1949, "Антиутопия", "ISBN-002", 328, "мягкая"),
        EBook("Мастер и Маргарита", "Булгаков", 1967, "Роман", "ISBN-003", "EPUB", 2.5),
        AudioBook("Евгений Онегин", "Пушкин", 1833, "Поэзия", "ISBN-004", 180, "Смоктуновский"),
    ]

    for book in initial_books:
        library.add_book(book)

    print("Библиотека инициализирована с 4 книгами")

    # Главный цикл программы
    while True:
        print_menu()
        choice = input("Выберите действие (0-8): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            take_book(library)
        elif choice == "3":
            find_by_isbn(library)
        elif choice == "4":
            find_by_author(library)
        elif choice == "5":
            find_by_genre(library)
        elif choice == "6":
            find_by_year(library)
        elif choice == "7":
            show_all_books(library)
        elif choice == "8":
            run_simulation()
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
