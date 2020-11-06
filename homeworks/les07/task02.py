"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 +0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """

from abc import abstractmethod


class Clothes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def outgo(self):
        pass


class Coat(Clothes):
    @property
    def outgo(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suite(Clothes):
    @property
    def outgo(self):
        return round(2 * self.size + 0.3, 2)


if __name__ == '__main__':
    kk_suit = Suite('KKlain', 48)
    hs_suit = Suite('Henderson', 50)
    hs_coat = Coat('Heresis', 44)
    ga_coat = Coat('Gloverall', 46)

    print(kk_suit.outgo)
    print(hs_suit.outgo)
    print(hs_coat.outgo)
    print(ga_coat.outgo)
