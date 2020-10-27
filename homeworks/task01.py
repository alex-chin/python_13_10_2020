"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

# первый параметр (название скрипта) пропускаем
_, param_produce_hours, param_rate, param_bonus = argv


def salary(produce_hours, rate, bonus):
    """ Простой расчет зарплаты
    :param produce_hours:
    :param rate:
    :param bonus:
    :return:
    """
    return produce_hours * rate + bonus


print('Зарплата : ', salary(int(param_produce_hours), int(param_rate), int(param_bonus)))
