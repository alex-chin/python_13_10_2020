"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def input_float():
    """ Запрашивает число у пользователя """
    buf = input('Введите число : ')
    try:
        return float(buf)
    except ValueError:
        print('Ошибка ввода. ')


def ai_divide(a, b):
    """ Принимает два числа, возвращает результат деления """
    # todo описание функции
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


a = input_float()
b = input_float()
print('Результат : ', ai_divide(a, b))
