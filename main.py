from utils import validate_params


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
