## Шифр Цезаря

- Python 3.11
- pytest
- mypy

### Тестирование и запуск

- Клонировать проект `git clone https://github.com/samsegomof/encrypt_decrypt_caesar`
- Активировать виртуальное окружение `source venv/bin/activate`
- Установить файл зависимостей `pip install -r requirements.txt`
- Для ручной проверки `python run.py`
- Для тестирования функции шифрования и дешифрования ввести в терминале `pytest`
- Для проверки аннотации типов ввести `mypy main.py`

### Описание

 - Функции шифрования и дешифрования реализуют алгоритм шифра Цезаря https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F 
 - Реализованы без использования сторонних библиотек и специальных методов
 - Проверки вынесены в отдельную функцию
 - Добавлена возможность тестировать из консоли/терминала
