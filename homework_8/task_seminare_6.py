# Напишите функцию, которая преобразует pickle файл,
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import csv
import pickle
from pathlib import Path


def pickle2csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write,
    ):
        data = pickle.load(f_read)
        print(data.items())
        keys = list(data.keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
        rows = []
        rows_items = {}
        for id, value in data.items():
            rows_items[id] = value
        rows.append(rows_items)
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    pickle2csv(Path('new_user.pickle'))