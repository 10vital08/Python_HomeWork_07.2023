# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

HEXADECIMAL_SYSTEM = 16

def transfer_to_the_system(number: int, system: int) -> str:
    result_sys_16: str = ''
    mod: str = ''

    while number:
        mod = str(number % system)
        result_sys_16 = mod + result_sys_16
        number //= system
    return result_sys_16

number: int = int(input('Введите целое число: '))
res_str: str = transfer_to_the_system(number, HEXADECIMAL_SYSTEM)

print(f"16-ричное представление с помощью моей функции = {res_str}")
print(f"16-ричное представление с помощью встроенной функции = {hex(number)[2:]}")