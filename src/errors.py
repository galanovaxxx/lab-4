class ValidationError(Exception):
    """Базовый класс для всех ошибок валидации"""
    pass


class NegativeNumberError(ValidationError):
    """Ошибка: отрицательное число или ноль"""
    def __init__(self, field_name: str, value):
        self.field_name = field_name
        self.value = value
        self.message = f"Поле '{field_name}' не может быть отрицательным или нулём (введено: {value})"
        super().__init__(self.message)


class LowercaseStartError(ValidationError):
    """Ошибка: строка начинается с маленькой буквы"""
    def __init__(self, field_name: str, value: str):
        self.field_name = field_name
        self.value = value
        self.message = f"Поле '{field_name}' должно начинаться с большой буквы (введено: '{value}')"
        super().__init__(self.message)


class ContainsDigitsError(ValidationError):
    """Ошибка: строка содержит цифры"""
    def __init__(self, field_name: str, value: str):
        self.field_name = field_name
        self.value = value
        self.message = f"Поле '{field_name}' не должно содержать цифры (введено: '{value}')"
        super().__init__(self.message)


class YearOutOfRangeError(ValidationError):
    """Ошибка: год вне допустимого диапазона"""
    def __init__(self, value: int, min_year: int = 1800, max_year: int = 2026):
        self.value = value
        self.min_year = min_year
        self.max_year = max_year
        self.message = f"Год должен быть от {min_year} до {max_year} (введено: {value})"
        super().__init__(self.message)


class EmptyStringError(ValidationError):
    """Ошибка: пустая строка"""
    def __init__(self, field_name: str):
        self.field_name = field_name
        self.message = f"Поле '{field_name}' не может быть пустым"
        super().__init__(self.message)


class ForbiddenSymbolError(ValidationError):
    """Ошибка: запрещённые символы в строке"""
    def __init__(self, field_name: str, value: str):
        self.field_name = field_name
        self.value = value
        self.message = f"Поле '{field_name}' содержит запрещённые символы (введено: '{value}')"
        super().__init__(self.message)


class NumberTooLargeError(ValidationError):
    """Ошибка: число слишком большое"""
    def __init__(self, field_name: str, value, max_value):
        self.field_name = field_name
        self.value = value
        self.max_value = max_value
        self.message = f"Поле '{field_name}' слишком большое (максимум: {max_value}, введено: {value})"
        super().__init__(self.message)


class InvalidCoverTypeError(ValidationError):
    """Ошибка: недопустимый тип обложки"""
    def __init__(self, value: str):
        self.value = value
        self.message = f"Тип обложки должен быть 'мягкая' или 'твёрдая' (введено: '{value}')"
        super().__init__(self.message)


class DuplicateBookError(ValidationError):
    """Ошибка: книга с таким ISBN уже существует"""
    def __init__(self, isbn: str):
        self.isbn = isbn
        self.message = f"Книга с ISBN '{isbn}' уже существует в библиотеке"
        super().__init__(self.message)


class EmptyLibraryError(ValidationError):
    """Ошибка: библиотека пуста"""
    def __init__(self):
        self.message = "Невозможно выполнить операцию: библиотека пуста"
        super().__init__(self.message)


class NotExistsError(ValidationError):
    """Ошибка: элемент не существует"""
    def __init__(self, field_name: str, value):
        self.field_name = field_name
        self.value = value
        self.message = f"{field_name} '{value}' не найден(а)"
        super().__init__(self.message)
