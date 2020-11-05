"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('task05.txt', 'w', encoding='utf-8') as file:
    # создать 1000 чисел
    file.write(' '.join([str(random.randint(100, 1000)) for i in range(1000)]))
with open('task05.txt', 'r', encoding='utf-8') as file:
    block = file.read()
    file_sum = 0
    for el in block.split():
        file_sum += int(el)
print("Сумма чисел в файле :", file_sum)
