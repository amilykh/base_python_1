# Задание 3
# Есть два файла users.csv и hobby.csv: в первом хранятся ФИО 
# пользователей сайта, а во втором — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один 
# пользователь, разделитель между значениями — запятая. Написать 
# код, загружающий данные из обоих файлов и формирующий из них 
# словарь: ключи — ФИО, значения — данные о хобби (список строковых
# переменных). Сохранить словарь в файл task_6_3_result.json. 
# Проверить сохранённые данные. Если в файле, хранящем данные 
# о хобби, меньше записей, чем в файле с ФИО, задаём в словаре
# значение None. Если наоборот — выходим из скрипта с кодом 1.
#
# При решении задачи считать, что объём данных в файлах во много
# раз меньше объема ОЗУ.
#
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, 
     разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные 
     запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    _keys = []
    _hobbies = []
    with open(path_users_file, 'r', encoding='utf-8') as fr_u:
        for _row in fr_u.readlines():
            _key_list = _row.strip().split(',')  # распаковка
            _key = " ".join(_key_list)
            _keys.append(_key)

    with open(path_hobby_file, 'r', encoding='utf-8') as fr_h:
        for _row in fr_h.readlines():
            _hobby_list = _row.strip().split(',')  # распаковка
            _hobbies.append(_hobby_list)

    if len(_keys) < len(_hobbies):  # либо завершите исполнение программы кодом 1
        print(f"ERROR: в файле {path_hobby_file}, хранящем данные о хобби,"
              f" меньше записей, чем в файле {path_users_file} с ФИО")
        sys.exit(1)
    else:  # либо верните словарь
        result_dict = dict.fromkeys(_keys)
        # result_dict = {key: value for key, value in zip(_keys, _hobbies)}
        for i in range(len(_hobbies)):
            result_dict[_keys[i]] = _hobbies[i]

    return result_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
