from typing import Optional

from validator import validate_params


def encrypting(text: str, shift: int) -> str:
    """
    Функция шифрования методом шифра Цезаря
    :param text: исходная строка для шифрования
    :type text: str
    :param shift: значение смещения для шифрования
    :type shift: int
    :return: зашифрованная строка
    :rtype: str
    """
    try:
        validate_params(text, shift)  # перед тем как зашифровать текст проходит все проверки с помощью валидатора
        encrypt_text = []  # пустой список для зашифрованного текста
        for symbol in text:
            if symbol.isalpha():  # проверяем, является ли символ буквой
                if symbol.islower():  # проверяем регистр символа
                    # переводим буквенные символы в значения unicode, отнимаем значение unicode буквы "a",
                    # прибавляем смещение, берем остаток от деления на 26 и прибавляем значение unicode буквы "a"
                    shifted_symbol = chr((ord(symbol) - ord("a") + shift) % 26 + ord("a"))
                else:
                    # аналогично для заглавных букв
                    shifted_symbol = chr((ord(symbol) - ord("A") + shift) % 26 + ord("A"))
                encrypt_text.append(shifted_symbol)  # добавляем текст с учетом сдвига в список

            else:
                encrypt_text.append(symbol)  # иначе добавляем символ как есть
        return "".join(encrypt_text)  # объединяем текст из списка в строку и возвращаем ее
    except (ValueError, TypeError) as e:
        return f"Error: {e}"


def decrypting(text: str, shift: int) -> str:
    """
    Функция дешифрования методом шифра Цезаря
    :param text: исходная строка для дешифрования
    :type text: str
    :param shift: значение смещения для дешифрования
    :type shift: int
    :return: дешифрованная строка
    :rtype: str
    """
    try:
        validate_params(text, shift)

        decrypt_text = []

        for symbol in text:
            if symbol.isalpha():
                if symbol.islower():
                    # при дешифровании - отнимаем смещение
                    shifted_symbol = chr((ord(symbol) - ord("a") - shift) % 26 + ord("a"))
                else:
                    shifted_symbol = chr((ord(symbol) - ord("A") - shift) % 26 + ord("A"))
                decrypt_text.append(shifted_symbol)

            else:
                decrypt_text.append(symbol)
        return "".join(decrypt_text)

    except (ValueError, TypeError) as e:
        return f"Error: {e}"
