"""
Напишите функцию группового переименования файлов. Она должна:
* -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* -- принимать параметр количество цифр в порядковом номере.
* -- принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
* -- принимать параметр расширение конечного файла.
* -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os

FINAL_NAME = "lol"
COUNT_DIGIT = 2


def rename_file(new_name: str, count_digit: int, old_extension: str, new_extension: str, range_simb: list):
    os.chdir('files')
    # список файлов в текущей директории
    all_files_directory = os.listdir()
    file_number = ''
    count = 0 # счётчик файлов

    if count_digit == 1:
        count = 1
    elif count_digit == 2:
        count = 9

    for file in all_files_directory:
        # количество символов старого имени, расширение старого имени
        count_char_old_name, expansion_old_file = file.split('.')

        # если такого расширения нет в списке файлов, то пропускаем итерацию
        if expansion_old_file != old_extension:
            continue

        # если в аргументах указали, с какого по какой символ нужно сохранить от старого имени, то формируем срез
        if len(range_simb) == 2:
            count += 1
            if len(count_char_old_name) > range_simb[1] - range_simb[0]:
                count_char_old_name = file[range_simb[0] - 1: range_simb[1]:]

        # вызываем метод переименования файла для склейки получившегося имени
        os.rename(file, f'{count_char_old_name}{FINAL_NAME}{count}.{new_extension}')


rename_file(FINAL_NAME, COUNT_DIGIT, "png", "txt", [2, 5])

# if __name__ == "__main__":
#     if rename_file(FINAL_NAME, COUNT_DIGIT, "png", "txt", [2, 5]):
#         print("Переименование прошло успешно")
#     else:
#         print("Вы допустили ошибку, к глубочайшему сожалению")
