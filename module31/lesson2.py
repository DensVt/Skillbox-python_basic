# Задача 1. Согласные
# Дан следующий текст:
# Even if they are djinns, I will get djinns that can outdjinn them.
# Используя регулярные выражения, напишите программу, которая выводит два списка:
# Первый содержит все слова, которые начинаются на гласную букву латинского алфавита (в этот раз слово может состоять и из одной буквы, например I).
# Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
# Для получения второго списка за основу используйте шаблон, которым вы получили первый список.

# Ещё небольшая подсказка: посмотрите, чем отличается символ * от символа +. Также, когда будете получать второй список, обратите внимание, на какой символ начинаются слова.

# Ожидаемый результат:
# Слова на гласную: ['Even', 'if', 'are', 'I', 'outdjinn']
# Слова на любой символ, кроме гласной: ['they', 'djinns', 'will', 'get', 'djinns', 'that', 'can', 'them']

import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
res = re.findall(r'\b[aeiouAEIOU]\w*', text)
print('Слова на гласную: ', res)

res = re.findall(r'\b[^aeiouAEIOU\W]\w*', text)
print('Слова на любой символ, кроме гласной: ', res)

# Задача 2. Даты
# Из одного дата-центра пришёл текстовый пакет данных, который содержит информацию о кодовом названии оборудования, его серийном номере и дате начала эксплуатации. Вот небольшой кусочек из этого пакета в виде строки:
# Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009

# Используя регулярные выражения, напишите программу, получающую список всех дат, которые встречаются в строке.
# Для этого необходимо использовать \d.
# Ожидаемый результат:
# ['12-05-2007', '11-11-2011', '12-01-2009']

string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
res = re.findall(r'\d{2}-\d{2}-\d{4}', string)
print(res)
