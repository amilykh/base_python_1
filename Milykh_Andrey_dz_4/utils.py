# Задание 2
#
# В корневой директории урока создать `task_4_2.py` и написать в нём
# функцию `currency_rates()`, принимающую в качестве аргумента код
# валюты (например, USD, EUR, SGD, ...) и возвращающую курс этой валюты
# по отношению к рублю.
#
# Использовать библиотеку `requests`. 
#
# В качестве API можно использовать `http://www.cbr.ru/scripts/XML_daily.asp`.
#
# > Рекомендация: выполнить предварительно запрос к API в обычном
#   браузере, посмотреть содержимое ответа.
#
# * Можно ли, используя только методы класса `str`, решить поставленную задачу?
#
# * Функция должна возвращать результат числового типа, например `float`. 
#
# Подумайте:
#
# * есть ли смысл для работы с денежными величинами использовать
#   вместо `float` тип `Decimal`?
#
# * Сильно ли усложняется код функции при этом?
#
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть `None`.  
#
# Можно ли сделать работу функции не зависящей от того, в каком
# регистре был передан аргумент?  
#
# В качестве примера выведите курсы доллара и евро.
#
# **ВНИМАНИЕ!** Используйте стартовый код для своей реализации:
#
from typing import Optional
from requests import get, utils


# def currency_rates(code: str) -> float:
# -----------------------------------------------------------------------------
# Если вы пометите переменную типом int и попытаетесь присвоить ей None,
# будет ошибка:#
#
# Incompatible types in assignment
# (expression has type "None", variable has type "int")
#
# Для таких случаев предусмотрена в модуле typing аннотация Optional с указанием
# конкретного типа. Обратите внимание, тип опциональной переменной указывается
# в квадратных скобках
# ------------------------------------------------------------------------------
def currency_rates(code: str) -> Optional[float]:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    _code = code.upper()
    _response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    _encodings = utils.get_encoding_from_headers(_response.headers)
    _content = _response.content.decode(encoding=_encodings)
    if _content.find(_code) == -1:
        return None
    _index_char_code = _content.find(_code)
    _index_value = _content.find("<Value>", _index_char_code)
    _start_course = _index_value+len("<Value>")
    _end_course = _content.find("</Value>", _index_char_code)
    _course_str_ru = _content[_start_course:_end_course]
    _course_str_en = _course_str_ru.replace(",", ".")
    # здесь должно оказаться результирующее значение float
    # result_value = float(course_str_en)
    return float(_course_str_en)


if __name__ == '__main__':
    print(currency_rates("USD"))
    print(currency_rates("eur"))
    print(currency_rates("noname"))
