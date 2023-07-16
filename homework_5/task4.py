"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci(num):
    fib = [0, 1]
    while num > 0:
        yield fib[-1]
        fib.append(fib[-1] + fib[-2])
        num -= 1


fibon = fibonacci(8)
list_fibon = iter(fibon)

print(*list_fibon)
