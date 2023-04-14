

def encryption_caesar(text: str, shift: int) -> str:
    """
    Функция шифрования методом шифра Цезаря.

    :param text: Исходная строка для шифрования.
    :type text: str
    :param shift: Смещение для шифрования
    :type shift: int
    :return: Зашифрованная строка
    :rtype: str
    """

    try:
        if not isinstance(text, str) or not isinstance(shift, int):
            raise TypeError("Некорректные типы аргументов. Ожидается str для 'text' и int для 'shift'.")

        if shift < 0:
            raise ValueError("Значение смещения 'shift' не может быть отрицательным")

        if not text:
            raise ValueError("Пустая строка передана в 'text'")

        if not text.strip():
            raise ValueError("Строка 'text' состоит только из пробельных символов")

        if shift > 25:
            raise ValueError("Значение смещения 'shift' должно быть в диапазоне от 0 до 25")

        encrypted_text = []
        for char in text:
            if char.isalpha():
                ascii_offset = ord("a") if char.islower() else ord("A")
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text.append(shifted_char)
            elif char.isdigit():
                shifted_digit = (int(char) + shift) % 10
                encrypted_text.append(str(shifted_digit))
            else:
                shifted_char = chr((ord(char) + shift))
                encrypted_text.append(shifted_char)
        return "".join(encrypted_text)

    except TypeError as e:
        print(f"Произошла ошибка типа: {e}")
    except ValueError as e:
        print(f"Произошла ошибка значения: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


def decryption_caesar(text: str, shift: int) -> str:
    pass

