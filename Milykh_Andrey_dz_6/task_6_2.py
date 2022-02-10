# Задание 2 *(вместо 1)
# Найти IP адрес спамера и количество отправленных им запросов 
# по данным файла логов из предыдущего задания.
#
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает 
# объем ОЗУ компьютера.

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """
    Парсит строку на атрибуты и возвращает кортеж атрибутов
    (<remote_addr>, <request_type>, <requested_resource>)
    """
    _line = line.split(' ')
    _remote_addr = _line[0]
    # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>
    return _remote_addr


def get_keys(d: dict, value: int) -> str:
    _keys = []
    for _key, _val in d.items():
        if _val == value:
            _keys.append(_key)
    return _keys


dict_clients = dict()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        _client = get_parse_attrs(row)
        if dict_clients.get(_client) == None:
            dict_clients[_client] = 1
        else:
            dict_clients[_client] += 1

max_requests  = max(dict_clients.values())
print(f'Клиенты, отравившие максимальное колчество запросов ({max_requests}):')
list_spammers = get_keys(dict_clients, max_requests)
for spammer in list_spammers:
    print(spammer)



