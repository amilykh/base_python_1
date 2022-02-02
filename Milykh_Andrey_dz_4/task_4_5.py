# Задание 5
# *(вместо 4) Рядом со скриптом `task_4_4.py`, создать скрипт
# `task_4_5.py` с содержимым аналогичным `task_4_4.py`, но 
# переработанным так, чтобы новый скрипт теперь срабатывал, 
# как `CLI`, прямо в консоли/терминале.
#
# Например:
#
# ```
#
# >>> python task_4_5.py USD
# 75.18, 2020-09-05
# ```
#
# > Задачи со * предназначены для продвинутых учеников, которым
# мало сделать обычное задание.
#
import argparse
import utils


def create_parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('currency', nargs='?')  # currency
    return _parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    # print (namespace)

    if namespace.currency:
        print(utils.currency_rates(namespace.currency))
    else:
        print("Пример вызова: python task_4_5.py USD")
"""
PS E:\projects\PycharmProjects\gb_python_homeworks\dz_4> python task_4_5.py
Пример вызова: python task_4_5.py USD
PS E:\projects\PycharmProjects\gb_python_homeworks\dz_4> python task_4_5.py USD
76.4849
PS E:\projects\PycharmProjects\gb_python_homeworks\dz_4> python task_4_5.py GBP
103.5988
PS E:\projects\PycharmProjects\gb_python_homeworks\dz_4>
"""
