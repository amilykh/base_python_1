# Урок 6. Работа с файлами
# Задание 1
# Не используя библиотеки для парсинга, распарсить (получить определённые данные) 
# файл логов web-сервера nginx_logs.txt — получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>) . Например:
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов
    (<remote_addr>, <request_type>, <requested_resource>)
    """
    _line = line.split(' ')
    _remote_addr = _line[0]
    _request_type = _line[5][1:]
    _requested_resource = _line[6]
    # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>
    return _remote_addr, _request_type, _requested_resource


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        list_out.append(get_parse_attrs(row))
pprint(list_out, indent=2)
