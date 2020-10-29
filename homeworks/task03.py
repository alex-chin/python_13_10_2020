"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('task03.txt', 'r', encoding='utf-8') as file:
    whole_sum = 0
    n = 0
    for line in file:
        l_line = line.split()
        if l_line[0] == '#':
            continue
        name = l_line[0]
        salary = int(l_line[1])
        n += 1
        whole_sum += salary
        if salary < 20000:
            print(name, salary)
    print(f"Средняя величина дохода : {whole_sum / n}")
