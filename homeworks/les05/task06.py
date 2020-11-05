"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import json


def filter_no_rem(lines):
    """ фильтр строк - удаление пустых и комментариев
    :param lines:
    :return:
    """
    for el in lines:
        if el[0] == '#' or el.strip() == '':
            continue
        yield el


def filter_int(words):
    """ преобразует слова с мусором в числа или 0
    :param words:
    :return:
    """
    for el in words:
        yield int('0' + ''.join([x for x in el if x.isdigit()]))


def repack_line(subject):
    """
    формирование строки в формате
    :param subject:
    :return:
    """
    return subject[0][:-1], sum(list(filter_int(subject[1:])))


with open("task06.txt", 'r', encoding='utf-8') as file:
    les = dict()
    for line in filter_no_rem(file.readlines()):
        key, hours = repack_line(line.split())
        les[key] = hours
    # красивая печать
    print(json.dumps(les, ensure_ascii=False, indent=4))
