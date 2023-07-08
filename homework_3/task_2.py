# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list_1 = [1, 2, 1, 2, 2, 5, 3, 6, 7, 7, 8, 2]
list_result = []

for i in list_1:
    if list_1.count(i) > 1 and i not in list_result:
        list_result.append(i)

print(list_result)