# task_7_4.py
import os
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
parsing_dir = 'some_dir'
folder = os.path.join(BASE_DIR, parsing_dir)


def create_dir(_dir_path: str):
    # Create target Directory if don't exist
    if not os.path.exists(_dir_path):
        os.mkdir(_dir_path)
        print(f'Directory {_dir_path} created')
    else:
        print(f"Directory {_dir_path} already exists")


def create_file_size(_file_name: str, _file_size: int):
    with open(_file_name, 'w', encoding='utf-8') as fw:
        if _file_size == 0:
            fw.seek(0)
        else:
            fw.seek(_file_size - 1)  # an example pick any size
        fw.write('\x00')
    # print(f"The file {_file_name} hase size {os.stat(_file_name).st_size}")


# создаём каталог с файлами для тестирования
create_dir(folder)
for i in range(15):
    number = round(random.random() * 10 ** 6, 3)
    file_size = random.randint(0, 100)
    create_file_size(os.path.join(folder, str(number)), file_size)
for i in range(3):
    number = round(random.random() * 10 ** 6, 3)
    file_size = random.randint(100, 1000)
    create_file_size(os.path.join(folder, str(number)), file_size)
for i in range(7):
    number = round(random.random() * 10 ** 6, 3)
    file_size = random.randint(1000, 10000)
    create_file_size(os.path.join(folder, str(number)), file_size)
for i in range(2):
    number = round(random.random() * 10 ** 6, 3)
    file_size = random.randint(10000, 100000)
    create_file_size(os.path.join(folder, str(number)), file_size)

# обход каталога с тестовыми файлами
dict_result = {}

size_threshold = 100
files = [item
         for item in os.scandir(folder)
         if item.stat().st_size < size_threshold]  # 0 <= st_size < size_threshold
dict_result[size_threshold] = len(files)

size_threshold = 1000
files = [item
         for item in os.scandir(folder)
         if 100 <= item.stat().st_size < size_threshold]  # 0 <= st_size < size_threshold
dict_result[size_threshold] = len(files)

size_threshold = 10000
files = [item
         for item in os.scandir(folder)
         if 1000 <= item.stat().st_size < size_threshold]  # 0 <= st_size < size_threshold
dict_result[size_threshold] = len(files)

size_threshold = 100000
# item = DirEntry   # генератор объектов
files = [item
         for item in os.scandir(folder)
         if 10000 <= item.stat().st_size < size_threshold]  # 0 <= st_size < size_threshold
dict_result[size_threshold] = len(files)

print(dict_result)
