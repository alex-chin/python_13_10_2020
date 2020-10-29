"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('task05.txt', 'w', encoding='utf-8') as file:
    rnd_int = [str(random.randint(100, 1000)) for i in range(100)]
    file.write(' '.join(rnd_int))
with open('task05.txt', 'r', encoding='utf-8') as file:
    pass
