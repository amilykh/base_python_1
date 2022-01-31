# Задание 4
# '''
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую
# в качестве аргументов строки в формате «Имя Фамилия» и возвращающую
# словарь, в котором ключи — первые буквы фамилий, а значения —
# словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы.
#
# Например:
#
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#    "А": {
#        "П": ["Петр Алексеев"]
#    },
#    "И": {
#        "И": ["Илья Иванов"]
#    },
#    "С": {
#        "И": ["Иван Сергеев", "Инна Серова"],
#        "А": ["Анна Савельева"]
#    }
# }
# Как поступить, если потребуется сортировка по ключам?
# '''


def get_unique_keys(keys: list) -> list:
    _unique = []

    for _key in keys:
        if _key in _unique:
            continue
        else:
            _unique.append(_key)
    return _unique


def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    _keys = []
    _names = []
    for _arg in args:
        _keys.append(_arg[:1])
        _names.append(_arg)
    _unique_keys = get_unique_keys(_keys)
    _unique_keys.sort()

    dict_out = {}  # результирующий словарь значений
    for _key in _unique_keys:
        _names_sample = filter(lambda el: el[0] in _key, _names)
        _accepted_names = list(_names_sample)
        _accepted_names.sort()

        dict_out[_key] = _accepted_names

    return dict_out


def thesaurus_adv(*args) -> dict:
    # пишите свою реализацию здесь
    _keys = []
    _names_surnames = []
    _names = []
    _surnames = []
    _surnames_names = []

    print(args)

    for _arg in args:
        # _names_surnames.append(_arg)
        _names.append(_arg.split(' ')[0])
        _surnames.append(_arg.split(' ')[1])
        _keys.append(_arg.split(' ')[1][:1])

    for _surname, _name in zip(_surnames, _names):
        _surnames_names.append(f'{_surname} {_name}')
     # print(_surnames_names)

    _surnames.clear()
    _names.clear()
    # print(_keys)
    # print(_names)
    # print(_surnames)

    _unique_keys = get_unique_keys(_keys)
    _unique_keys.sort()
    # print(_unique_keys)
    # print(_names_surnames)

    dict_out = {}  # результирующий словарь значений

    for _key in _unique_keys:
        _surnames_names_sample = filter(lambda el: el[0] in _key,
                                        _surnames_names)
        _accepted_surnames_names = list(_surnames_names_sample)
        _accepted_surnames_names.sort()
        # print(_key, _accepted_surnames_names)

        _surnames.clear()
        _names.clear()
        for item in _accepted_surnames_names:
            _surnames.append(item.split(' ')[0])
            _names.append(item.split(' ')[1])

        _names_surnames.clear()
        for _name, _surname in zip(_names, _surnames):
            _names_surnames.append(f'{_name} {_surname}')
        # print(_names_surnames)

        dict_out[_key] = thesaurus(*_names_surnames)

    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
