def validate_params(text: str, shift: int):
    if not isinstance(text, str):
        raise TypeError("Wrong type of text")
    if not isinstance(shift, int):
        raise TypeError("Wrong type of shift")
    if shift < 0 or shift > 25:
        raise ValueError("Shift should be between 0 and 25")
    if text is None or text == "":
        raise ValueError("Text should be not empty or none")
    if not text.strip():
        raise ValueError("Text should not contain only spaces")
    for char in text:
        if char.isalpha() and "а" <= char <= "я" or "А" <= char <= "Я":
            raise ValueError("Cyrillic characters is not supported")


def encrypting(text: str, shift: int) -> str:
    try:
        validate_params(text, shift)
        encrypt_text = []
        for symbol in text:
            if symbol.isalpha():
                if symbol.islower():
                    shifted_symbol = chr((ord(symbol) - ord("a") + shift) % 26 + ord("a"))
                else:
                    shifted_symbol = chr((ord(symbol) - ord("A") + shift) % 26 + ord("A"))
                encrypt_text.append(shifted_symbol)
            elif symbol.isdigit():
                shifted_symbol = chr((ord(symbol) - ord("0") + shift) % 10 + ord("0"))
                encrypt_text.append(shifted_symbol)
            else:
                shifted_symbol = chr(ord(symbol) + shift)
                encrypt_text.append(shifted_symbol)
        return "".join(encrypt_text)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"


def decryption_caesar(text: str, shift: int) -> str:
    pass


result = encrypting("Прикинь", 2)
print(result)

