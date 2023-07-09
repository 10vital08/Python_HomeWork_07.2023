# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут
# в рюкзак, передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

# определение списка помещаемых предметов
def add_to_backpack(max_cargo, you_dict):
    weight = 0
    res_list = []
    while weight <= max_cargo:
        for item in you_dict:
            if weight + you_dict[item] <= max_cargo:
                res_list.append(item)
                weight += you_dict[item]
        break
    return res_list, weight

# перевод списка вещей в строку
def list_to_string(my_list):
    string_res = ''
    string_res += ', '.join(my_list)

    return string_res

my_dict = {'Вода': 2, 'Еда': 1.2, 'Одежда': 1, 'Гиря': 4, 'Гаджеты': 0.5, 'Покрывало': 0.3}
max_backpack_cargo = float(input('Задайте максимальную грузоподъёмность: '))
string_result = ''

result = add_to_backpack(max_backpack_cargo, my_dict)
string_result = list_to_string(result[0])

print(f"Итого вес рюкзака составляет {result[1]} кг, "
      f"его состав: {string_result}")