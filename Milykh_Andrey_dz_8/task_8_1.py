# task_8_1.py
# Задание 1
# Написать тело функцию email_parse(email: str), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен
# из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.
import re
from typing import Union, Dict


def email_parse(email: str) -> Union[Dict[str, str], ValueError]:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    # pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
    re_mail = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
    try:
        result = re_mail.match(email)
        if result:
            _email = result.group(0)
            email_parts = _email.split('@')
            return {'username': email_parts[0], 'domain': email_parts[1]}
        else:
            raise ValueError
    except ValueError as e:
        print(f"ValueError: wrong email: {email}")


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
