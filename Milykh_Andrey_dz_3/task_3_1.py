# Задание 1
#
# Написать функцию num_translate(), переводящую числительные
# от 0 до 10 c английского на русский язык.
#
# Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None.
#
# Подумайте, как и где лучше хранить информацию, необходимую
# для перевода: какой тип данных выбрать, в теле функции или снаружи.


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


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("twenty"))
