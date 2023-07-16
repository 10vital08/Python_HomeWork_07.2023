"""
Задание №6
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""

COUNT_RAW = 9
A = 0
B = 28
STEP = 9


def print_table(tab, a, b):
    for i in range(a, b, STEP):
        print(table[i], end='\t\t')
    print()


table = [f"{i} * {j} = {i * j}" for i in range(2, 10) for j in range(2, 11)]
# format_table = iter(table)
# print(*format_table, sep='\t')

# Вывод от 2х2 до 5х10
for i in range(COUNT_RAW):
    print_table(table, A, B)
    A += 1
    B += 1

print()

A = 36
B = 64

# Вывод от 6х2 до 9х10
for i in range(COUNT_RAW):
    print_table(table, A, B)
    A += 1
    B += 1
