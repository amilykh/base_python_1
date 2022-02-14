# task_7_3.py
import os
import shutil
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
parsing_dir = 'templates'
config_path = 'config.yaml'


def create_file(file_path: str):
    # Create target File if don't exist
    if not os.path.exists(file_path):
        # create a file
        try:
            # The default umask is 0o22 which turns off write permission of group and others
            # with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fw:
            with open(file_path, 'x', encoding='utf-8') as fw:
                # uncomment if you want empty file
                fw.write(f"This is  {file_path}")
        except Exception as e:
            print(f'Global error: {e}')
    else:
        print(f"File {file_path} already exists")


def create_dir(_dir_path: str):
    # Create target Directory if don't exist
    if not os.path.exists(_dir_path):
        os.mkdir(_dir_path)
        print(f'Directory {_dir_path} created')
    else:
        print(f"Directory {_dir_path} already exists")


def create_design(design: list):
    for _part in design:
        _part_lst = _part.split(',')
        path_name = os.path.join(_part_lst[1].replace("root", BASE_DIR), _part_lst[2])

        if _part_lst[0] == 'd':
            create_dir(path_name)
        elif _part_lst[0] == '-':
            create_file(path_name)
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


def get_path_project(design: list):
    _part = design[0]  # 1-я строка конфигурационного файла
    _part_lst = _part.split(',')
    return os.path.join(_part_lst[1].replace("root", BASE_DIR), _part_lst[2])


def copy_walk_dirs(out_parsing_dir: str, dirs: list):
    for _dir in dirs:
        src = os.path.join(out_parsing_dir, _dir)  # Source path
        dest = os.path.join(path_parsing_dir, _dir)  # Destination path
        destination = shutil.copytree(src, dest)  # Copy the content fo source to destination
        print(f"Destination path: {destination}")  # Print path of newly created file


path_project = get_path_project(open_design(config_path))
path_parsing_dir = os.path.join(path_project, parsing_dir)
create_dir(path_parsing_dir)
for dir_path, dir_names, file_names in os.walk(path_project):
    walk_dir_path = str(dir_path)
    if walk_dir_path == path_parsing_dir:  # директория, созданная программой, исключается из рекурсивного обхода
        continue
    end_path = walk_dir_path[walk_dir_path.rfind("\\") + 1:]
    walk_dir_names = list(dir_names)
    if end_path == parsing_dir and walk_dir_names:
        copy_walk_dirs(walk_dir_path, list(dir_names))
