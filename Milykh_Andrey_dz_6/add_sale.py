# -*- coding: UTF-8 -*-
import argparse
# import locale


def create_parse():
    _parser = argparse.ArgumentParser(
        description='''Запуск программы  из командной строки  >>>  python add_sale.py XXXX.X где
XXXX.X - число с плавающей точкой типа float, а X - цифра от 0 до 9'''
    )
    _parser.add_argument('sales_amount_float', nargs='?', type=float)
    return _parser


if __name__ == '__main__':
    # locale.setlocale(locale.LC_NUMERIC, 'rus')
    # print(locale.getlocale())
    parser = create_parse()
    namespace = parser.parse_args()
    # print (namespace)
    if not namespace.sales_amount_float:
        print(f"HELP: запуск программы ... >>> python add_sale.py XXXX.X"
              f" где X-цифра от 0 до 9")
    else:  # Записываем сумму  в файл
        _sales_amount = namespace.sales_amount_float
        with open('bakery.csv', 'a', encoding='utf-8') as fa:
            fa.write(str(_sales_amount).replace(".", ",") + "\n")
