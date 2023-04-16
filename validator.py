from typing import Any

from constants import SPEC_CHARS


def validate_params(text: str, shift: int) -> Any:
    """
    Функция для проверки параметров и обработки ошибок
    :param text: строка для шифрования/дешифрования
    :rtype text: str
    :param shift: смещение
    :rtype shift: int
    :raises: TypeError, ValueError
    """
    if not isinstance(text, str):
        raise TypeError("Wrong type of text")
    if not isinstance(shift, int):
        raise TypeError("Wrong type of shift")
    if shift < 0 or shift > 25:
        raise ValueError("Shift should be between 0 and 25")
    if text == "":
        raise ValueError("Text should be not empty")
    if not text.strip():
        raise ValueError("Text should not contain only spaces")
    for char in text:
        if char.isalpha() and "а" <= char <= "я" or "А" <= char <= "Я":
            raise ValueError("Cyrillic characters does not supported")
        if char in SPEC_CHARS:
            raise(ValueError("Special characters does not supported"))
        if char.isdigit():
            raise ValueError("Digits does not supported")
