"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} помечает')


if __name__ == '__main__':
    pen = Pen('Kaweco')
    pen.draw()
    pencil = Pencil('Koh-i-noor')
    pencil.draw()
    handle = Handle('Centropen')
    handle.draw()
