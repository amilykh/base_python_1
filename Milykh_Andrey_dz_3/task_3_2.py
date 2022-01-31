# Задание 2
#
# (вместо задачи 1) Перепишите функцию из задания 1 изменив
# название на num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы — результат
# тоже должен быть с заглавной.
#
# Например:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    _dict_of_numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if isinstance(_dict_of_numbers.get(value), str):
        return _dict_of_numbers.get(value)
    else:
        return str(_dict_of_numbers.get(value))


def num_translate_adv(value: str) -> str:
    _bool_title = value.istitle()
    if _bool_title is False:
        return num_translate(value)
    else:
        _value = value.lower()
        return num_translate(_value).title()


print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("Twenty"))
print(num_translate_adv("twenty"))
