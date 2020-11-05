"""
Подготовка данных к упражнению из http://generatedata.com/
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

"""

with open('task07.txt', 'r', encoding='utf-8') as file:
    out_lines = list()
    for line in file.readlines():
        words = line.split('|')
        out_lines.append('_'.join(words[0].split()) + ' ' + ' '.join(words[1:]))
with open('task07in.txt', 'w', encoding='utf-8') as file:
    file.writelines(out_lines)
