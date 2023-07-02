# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

number_1 = int(input('Задайте число от 1 до 999: '))
count_numbers = 0
min_number = 1
max_number = 999
border_one_numbers = 9 #граница цифр
border_two_numbers = 99 #граница двузначных чисел
string_result = ''
numerical_result = '' # результат вычислений
temp = 0 # временный буфер

# разворот строки
def reserved_3(variable):
    res = ''.join(reversed(variable))
    return res

if number_1 < min_number or number_1 > max_number:
    string_result = 'Введите заново число в диапазоне 1 - 999'

if number_1 >= min_number and number_1 <= border_one_numbers:
    string_result = 'Цифра. Квадрат = '
    numerical_result = number_1 ** 2

if number_1 > border_one_numbers and number_1 <= border_two_numbers:
    string_result = 'Двузначное число. Произведение цифр = '
    temp = [int(a) for a in str(number_1)] # разбиение на цифры в список
    numerical_result = 1 # переопределение переменной для умножения
    for i in temp:
        numerical_result *= i

if number_1 > border_two_numbers and number_1 <= max_number:
    string_result = 'Трёхзначное число. Зеркальное отображение числа = '
    temp = str(number_1)
    string_result = string_result + reserved_3(temp)

print(string_result + str(numerical_result))