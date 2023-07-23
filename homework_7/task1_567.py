from contextlib import chdir
from pathlib import Path

# Задача 5

# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import randint, choice

DIC1 = "GHIGYUGKJ"
DIC2 = "HIUHGYGHUGKJHI"


def function_ext(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30:
                    break
                name += choice(DIC2)
            name = name + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function_ext(dic, a=5, b=30, c=7, d=256)



# Задача 6

# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import randint, choice

DIC1 = "GHIGYUGKJ"
DIC2 = "HIUHGYGHUGKJHI"


def function_dir(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            if Path(name).is_file():
                continue
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function_dir(dic, a=5, b=30, c=7, d=256)

def dir(text):
    if isinstance(text, str):
        a = Path(text)
    else:
        a = text
    if not a.is_dir():
        a.mkdir(parents=True)
    chdir(a)
    function_dir(dic, a=5, b=30, c=7, d=256)

dir('Sem7')



# Задача 7

# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п..
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

def sort_file(dict_file_extension, dir_name):
    if isinstance(dir_name, str):
        dir_name = Path(dir_name)
    else:
        dir_name = dir_name
    chdir(dir_name)
    for key in dict_file_extension:
        a = Path(key)
        if not a.is_dir():
            a.mkdir(parents=True)

    p = Path(Path().cwd())
    for obj in p.iterdir():
        for key in dict_file_extension:
            if obj.suffix in dict_file_extension[key]:
                obj.replace(p / key / obj.name)

put = 'C:/'
dict_file_extension = {'video': ['.mov', '.avi', '.doc', '.mp4'], 'docum': ['.txt']}
sort_file(dict_file_extension, put)