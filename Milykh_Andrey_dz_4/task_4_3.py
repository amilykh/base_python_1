# Задание 3
# *(вместо 2) В `task_4_3.py` создать функцию `currency_rates_adv()` 
# аналогичную `currency_rates()` прошлого задания, только теперь
# она должна возвращать кроме курса ещё и дату, 
# которая передаётся в ответе сервера. 
#
# > Дата должна быть в виде объекта `date`. Т.е. функция должна 
# > возвращать кортеж из двух > элементов следующих типов
#  Decimal(используем вместо float) и datetime.date
#
# Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?
#
# **ВНИМАНИЕ!** Используйте стартовый код для своей реализации:
#
import datetime
from typing import Optional
from decimal import Decimal
from requests import get, utils


def currency_rates_adv(code: str) -> (Optional[Decimal], datetime):
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

    _start_date = _content.find('<ValCurs Date="') + len('ValCurs Date="') + 1
    _date_day = _content[_start_date:_start_date+2]
    _date_month = _content[_start_date+3:_start_date+5]
    _date_year = _content[_start_date+6:_start_date+10]
    _date_time_str = f"{_date_year}-{_date_month}-{_date_day} 00:00:00.000000"
    print(_date_time_str)
    _date_time_obj = datetime.datetime.strptime(_date_time_str, '%Y-%m-%d %H:%M:%S.%f')

    # здесь должно оказаться результирующее значение Decimal(используем вместо float)
    # result_value = Decimal(course_str_en)
    return Decimal(_course_str_en), _date_time_obj.date()


kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, Decimal):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
