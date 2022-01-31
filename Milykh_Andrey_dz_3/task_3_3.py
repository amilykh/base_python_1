# Задание 3
#
# Написать функцию thesaurus(), принимающую в качестве аргументов
# имена сотрудников и возвращающую словарь, в котором ключи — первые
# буквы имён, а значения — списки, содержащие имена, начинающиеся
# с соответствующей буквы.
#
# Например:
#
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
# Подумайте:
#
# * полезен ли будет вам оператор распаковки?
# * Как поступить, если потребуется сортировка по ключам?
# * Можно ли использовать словарь в этом случае?


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


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
