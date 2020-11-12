"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_range(start, end, step):
    """ частичная реализация range
    :param start:
    :param end:
    :param step:
    :return:
    """
    while start < end:
        yield start
        start += step


def my_reduce(func, li):
    """
    Частичная реализация reduce
    :param func:
    :param li:
    :return:
    """
    s = li[0]
    for el in li[1:]:
        s = func(s, el)
    return s


a = [x for x in my_range(100, 1000 + 2, 2)]
b = my_reduce((lambda prev, mul: prev * mul), a)

print("Произведение : ", b)
print("Количество разрядов : ", len(str(b)))
print("Хеш : ", hash(b))
