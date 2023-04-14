def encryption_caesar(text: str, shift: int) -> str:
    """
    Функция шифрования методом шифра Цезаря.
    
    :param text: Исходная строка для шифрования.
    :type text: str
    :param shift: Смещение для шифрования.
    :type shift: int
    :return: Зашифрованная строка.
    :rtype: str
    """
    if not isinstance(text, str) or not isinstance(shift, int):
        raise TypeError("Некорректные типы аргументов. Ожидается str для 'text' и int для 'shift'.")
    if not text:
        raise ValueError("Пустая строка передана в 'text'.")
    if not text.strip():
        raise ValueError("Строка 'text' состоит только из пробельных символов.")
    if shift < 0 or shift > 25:
        raise ValueError("Значение смещения 'shift' должно быть в диапазоне от 0 до 25.")
    
    encrypted_text = []
    for char in text:
        if char.isalpha():  
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text.append(shifted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def decryption_caesar(text: str, shift: int) -> str:
    """
    Функция дешифрования методом шифра Цезаря.
    
    :param text: Зашифрованная строка для дешифрования.
    :type text: str
    :param shift: Смещение для дешифрования.
    :type shift: int
    :return: Исходная строка.
    :rtype: str
    """
    if not isinstance(text, str) or not isinstance(shift, int):
        raise TypeError("Некорректные типы аргументов. Ожидается str для 'text' и int для 'shift'.")
    if not text:
        raise ValueError("Пустая строка передана в 'text'.")
    if not text.strip():
        raise ValueError("Строка 'text' состоит только из пробельных символов.")
    if shift < 0 or shift > 25:
        raise ValueError("Значение смещения 'shift' должно быть в диапазоне от 0 до 25.")
    
    decrypted_text = []
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text.append(shifted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)