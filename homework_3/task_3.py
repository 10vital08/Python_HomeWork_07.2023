# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
import re
from collections import Counter

# def top_words_10(text_top):
#     words = re.findall(r'\b\w+\b', text_top)
#     return Counter(words).most_common(10)

# удаление точек, запятых и скобок из текста
def remove_extra_characters(list_text):
    temp_text = ''
    for i in range(0, len(list_text)):
        if list_text[i] != '.' and list_text[i] != '(' and list_text[i] != ')'\
            and list_text[i] != ',':
            temp_text += list_text[i]
    return temp_text

# def

text = ', , , ,,(Большая часть работы) программистов связана с написанием исходного кода,' \
       ' тестированием и отладкой программ на одном из языков программирования. ' \
       'Исходные тексты и исполняемые файлы программ являются объектами авторского ' \
       'права и являются интеллектуальной собственностью их авторов и правообладателей. '\
       'Различные языки программирования поддерживают различные стили программирования'

# перевод строки в нижний регистр
text = text.lower()
print(text)

new_text = remove_extra_characters(text)
print(new_text)

# delimiters = ' \n\t\r\b,' # символы для исключения
# list_text = re.split('|'.join(delimiters), text)
#
# print(list_text)