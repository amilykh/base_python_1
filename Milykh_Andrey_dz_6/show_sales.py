import sys
import argparse
# import locale


def create_parse():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('start_row', nargs='?', type=int)
    _parser.add_argument('end_row', nargs='?', type=int)

    return _parser


if __name__ == '__main__':
    # locale.setlocale(locale.LC_NUMERIC, 'rus')
    # print(locale.getlocale())
    parser = create_parse()
    namespace = parser.parse_args()

    print(namespace)

    if namespace.start_row is None:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            content = fr.read()
            print(content)
    elif namespace.end_row is None:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            lines = 0
            for line in fr:
                lines += 1

            if namespace.start_row > lines:
                print(f"ERROR: номер стартовой строки {namespace.start_row} не может"
                      f" быть больше {lines} - количества строк в файле!")
                sys.exit(1)

            fr.seek(0)  # устанавливаем курсор в начало файла!
            for _ in range(namespace.start_row - 1):  # нумерация строк с 1 !!! Устанавливаем
                fr.readline()  # курсор в начало строки start_row
            line = fr.readline()
            while line:
                print(line.strip(), sep='\n')
                line = fr.readline()
    else:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            lines = 0
            for line in fr:
                lines += 1

            if namespace.start_row > lines:
                print(f"ERROR: номер стартовой строки {namespace.start_row} не может"
                      f" быть больше {lines} - количества строк в файле!")
                sys.exit(1)
            if namespace.end_row > lines:
                print(f"ERROR: номер конечной строки {namespace.end_row} не может"
                      f" быть больше {lines} - количества строк в файле!")
                sys.exit(1)
            if namespace.end_row < namespace.start_row:
                print(f"ERROR: номер конечной строки - {namespace.end_row}, не может"
                      f" быть меньше номера начальной строки - {namespace.start_row} !")
                sys.exit(1)

            fr.seek(0)  # устанавливаем курсор в начало файла!
            for _ in range(namespace.start_row - 1):  # нумерация строк с 1 !!! Устанавливаем
                fr.readline()  # курсор в начало строки start_row
            count = namespace.end_row - namespace.start_row + 1
            line = fr.readline()
            while count > 0:
                print(line.strip(), sep='\n')
                line = fr.readline()
                count -= 1
