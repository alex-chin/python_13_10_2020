"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dict_int = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре'}
with open('task04.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
with open('task04out.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        l_line = line.split()
        if len(l_line) == 3:
            l_line[0] = dict_int.get(l_line[0].lower(), '?????').title()
            line = ' '.join(l_line)
            file.write(line + '\n')
