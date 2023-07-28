# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
import os


def direct(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as file:
        res_n = json.load(file)
        file.close()

    with open(f'{name}.pickle', 'wb') as writes:
        res_a = pickle.dump(res_n, writes)
        writes.close()


all_files_directory = os.listdir()
for file in all_files_directory:
    if len(file.split('.')) <= 1:
        continue
    expansion_file = file.split('.')[1]
    if expansion_file != "json":
        continue
    direct(file.split('.')[0])