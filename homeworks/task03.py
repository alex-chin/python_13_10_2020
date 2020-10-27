"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


def my_range(start, end, step=1):
    """ частичная реализация range
    :param start:
    :param end:
    :param step:
    :return:
    """
    while start < end:
        yield start
        start += step


# 1 вариант - в лоб
a1 = [x for x in my_range(20, 240) if not (x % 20) or not (x % 21)]

# 1 вариант эффективный - ленивый
a2 = [x for x in my_range(20, 240, 20)] + [x for x in my_range(21, 240, 21)]

# 2 вариант эффективный - жадный
a3 = [x for x in list(my_range(20, 240, 20)) + list(my_range(21, 240, 21))]

print("Список чисел, кратных 20 и 21", a1)
print("Список чисел, кратных 20 и 21", a2)
print("Список чисел, кратных 20 и 21", a3)
