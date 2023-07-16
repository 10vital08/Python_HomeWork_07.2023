# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def return_dictonary(**kwargs):
    res_dict = {}

    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset)):
            value = str(value)

        res_dict[value] = key

    return res_dict


dict_result = return_dictonary(математика=[1, 2], физика=4)

print(dict_result)
