from main import encrypting, decrypting


def run():
    while True:
        print("Добро пожаловать в шифратор/дешифратор методом Цезаря!")
        print("Выберете режим:\nE - шифрования\nD - дешифрования")
        choose = input()
        if choose == "E" or choose == "e":
            try:
                text = input("Введите текст для шифрования:\n")
                shift = int(input("Введите значение шага для шифрования:\n"))
                encrypted_text = encrypting(text, shift)
                print(f"Зашифрованный текст: {encrypted_text}")
            except Exception as e:
                return e
        if choose == "D" or choose == "d":
            try:
                text = input("Введите текст для дешифрования:\n")
                shift = int(input("Введите значение шага для дешифрования:\n"))
                decrypted_text = decrypting(text, shift)
                print(f"Дешифрованный текст: {decrypted_text}")
            except Exception as e:
                return e


if __name__ == "__main__":
    run()
