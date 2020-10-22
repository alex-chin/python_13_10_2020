"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    # todo описание функции
    if a > c and b > c:
        return a + b
    elif b > a and c > a:
        return b + c
    else:
        return a + c


print(my_func(1, 2, 3))
print(my_func(1, 2, 3))
print(my_func(1, 3, 2))
