# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

HEXADECIMAL_SYSTEM = 16
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'

def transfer_to_the_system(number: int, system: int) -> str:
    result_sys_16: str = ''
    mod: str = ''

    while number:
        mod = str(number % system)
        if mod == '10':
            result_sys_16 = A + result_sys_16
        elif mod == '11':
            result_sys_16 = B + result_sys_16
        elif mod == '12':
            result_sys_16 = C + result_sys_16
        elif mod == '13':
            result_sys_16 = D + result_sys_16
        elif mod == '14':
            result_sys_16 = E + result_sys_16
        elif mod == '15':
            result_sys_16 = F + result_sys_16
        else:
            result_sys_16 = mod + result_sys_16

        number //= system
    return result_sys_16

number: int = int(input('Введите целое число: '))
res_str: str = transfer_to_the_system(number, HEXADECIMAL_SYSTEM)

print(f"16-ричное представление с помощью моей функции = {res_str}")
print(f"16-ричное представление с помощью встроенной функции = {hex(number)[2:]}")