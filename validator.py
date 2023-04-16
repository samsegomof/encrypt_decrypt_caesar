from typing import Any

from constants import SPEC_CHARS


def validate_params(text: str, shift: int) -> Any:  # Возвращает Any только лишь чтобы mypy не ругался
    """
    Функция для проверки параметров и обработки ошибок
    :param text: строка для шифрования/дешифрования
    :rtype text: str
    :param shift: смещение
    :rtype shift: int
    :raises: TypeError, ValueError
    """
    if not isinstance(text, str):  # проверка типа аргумента text
        raise TypeError("Wrong type of text")
    if not isinstance(shift, int):  # проверка типа аргумента shift
        raise TypeError("Wrong type of shift")
    if shift < 0 or shift > 25:  # проверка значения shift - должно быть в диапазоне от 0 до 25
        raise ValueError("Shift should be between 0 and 25")
    if text == "":  # проверка на пустой text
        raise ValueError("Text should be not empty")
    if not text.strip():  # проверка на переданные в поле text только пробелы
        raise ValueError("Text should not contain only spaces")
    for char in text:
        if char.isalpha() and "а" <= char <= "я" or "А" <= char <= "Я":  # проверка на кириллицу
            raise ValueError("Cyrillic characters does not supported")
        if char in SPEC_CHARS:  # проверка на введенные спецсимволы
            raise(ValueError("Special characters does not supported"))
        if char.isdigit():  # проверка на введенные цифры
            raise ValueError("Digits does not supported")
