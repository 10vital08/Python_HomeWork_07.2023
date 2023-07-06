# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму
# и произведение дробей. Для проверки своего кода используйте модуль fractions.
import fractions

def operations_with_fractions(frac_1, frac_2):
    # преобразование дробей из строк в числа
    num_1, denom_1 = map(int, frac_1.split('/'))
    num_2, denom_2 = map(int, frac_2.split('/'))

    # вычисление суммы дробей
    summ_fraction_num = num_1 * denom_2 + num_2 * denom_1
    sum_fraction_denom = denom_1 * denom_2
    # скромное сокращение дроби
    if summ_fraction_num == sum_fraction_denom:
        summ_fraction_num = 1
        sum_fraction_denom = 1
    summ_fraction = (summ_fraction_num, sum_fraction_denom)

    # вычисление произведения дробей
    multiplication_fraction_num = num_1 * num_2
    multiplication_denom = denom_1 * denom_2
    # скромное сокращение дроби
    if multiplication_fraction_num == multiplication_denom:
        multiplication_fraction_num = 1
        multiplication_denom = 1
    multiplication_fraction = (multiplication_fraction_num, multiplication_denom)

    return summ_fraction, multiplication_fraction


fraction_1: str = input('Введите первую дробь: ')
fraction_2: str = input('Введите первую дробь: ')

sum_frac, mult_frac = operations_with_fractions(fraction_1, fraction_2)

# f1 = fractions.Fraction(2, 5)
# f2 = fractions.Fraction(3, 5)

print(f"Сумма дробей {fraction_1} и {fraction_2} = {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {fraction_1} и {fraction_2} = {mult_frac[0]}/{mult_frac[1]}")

# print(f"Сумма дробей с помощью встроенной функции = {f1 + f2}")
# print(f"Произведение дробей с помощью встроенной функции = {f1 * f2}")