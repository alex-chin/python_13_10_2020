"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    if a > c and b > c:
        return a + b
    elif b > a and c > a:
        return b + c
    else:
        return a + c
