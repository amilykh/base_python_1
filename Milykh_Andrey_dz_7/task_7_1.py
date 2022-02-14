# task_7_1.py
import os
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))


def create_dir(dir_path: str):
    # Create target Directory if don't exist
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print(f'Directory {dir_path} created')
    else:
        print(f"Directory {dir_path} already exists")


def create_design(design: list):
    for _part in design:
        _part_lst = _part.split(',')
        path_name = os.path.join(_part_lst[1].replace("root", BASE_DIR), _part_lst[2])

        if _part_lst[0] == 'd':
            create_dir(path_name)
        elif _part_lst[0] == '-':
            print(f"Создание файла...")
        else:
            print("ERROR: неверный формат файла конфигурации!")
            exit(1)


def open_design(f_path) -> list:
    """Функця считывания конфигурации проекта"""
    try:
        with open(f_path, 'r', encoding='utf-8') as fr:
            content = fr.read()
            return content.splitlines()
    except Exception as e:
        print(f'{e.__class__.__name__}: Поймали ошибку: {e}')


create_design(open_design('task_7_1.cfg'))
