from typing import Optional

from validator import validate_params


def encrypting(text: str, shift: int) -> Optional[str]:
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

            else:
                encrypt_text.append(symbol)
        return "".join(encrypt_text)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"


def decrypting(text: str, shift: int) -> str:
    try:
        validate_params(text, shift)

        decrypt_text = []

        for symbol in text:
            if symbol.isalpha():
                if symbol.islower():
                    shifted_symbol = chr((ord(symbol) - ord("a") - shift) % 26 + ord("a"))
                else:
                    shifted_symbol = chr((ord(symbol) - ord("A") - shift) % 26 + ord("A"))
                decrypt_text.append(shifted_symbol)

            else:
                decrypt_text.append(symbol)
        return "".join(decrypt_text)

    except (ValueError, TypeError) as e:
        return f"Error: {e}"
