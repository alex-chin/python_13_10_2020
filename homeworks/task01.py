"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def input_float():
    buf = input('Введите число : ')
    try:
        return float(buf)
    except ValueError:
        print('Ошибка ввода. ')


def ai_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')
    # except TypeError:
    #     print('Введены неправильные данные')


a = input_float()
b = input_float()
print('Результат : ', ai_divide(a, b))
