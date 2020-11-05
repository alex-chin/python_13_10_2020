"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def input_float(invite='Введите число : '):
    buf = input(invite)
    try:
        return float(buf)
    except ValueError:
        print('Ошибка ввода. ')


def input_int(invite='Введите число : '):
    buf = input(invite)
    try:
        return int(buf)
    except ValueError:
        print('Ошибка ввода. ')


def reverse_expo(x, neg_exp):
    """ Вычисляет отцательную степень числа """
    multi = x
    for _ in my_range(1, abs(neg_exp) - 1):
        multi *= x
    return 1 / multi


def my_range(start, end):
    """ Реализация простого варианта функции range"""
    while start <= end:
        yield start
        start += 1


x = input_float('Введите действительное положительное число : ')
neg_exp = input_int('Введите целое отрицательное число : ')
print('Результат', reverse_expo(x, neg_exp))
