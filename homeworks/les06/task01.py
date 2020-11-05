"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep


class TrafficLight:
    # контрольный автомат состояний
    chain_states = {'красный': 'желтый', 'желтый': 'зеленый', 'зеленый': 'красный'}
    chain_prev = ''

    def __init__(self):
        self.__color = ''

    def _check_color(self, color):
        is_good = False
        if self.chain_prev == '':
            is_good = True
        else:
            # контроль перехода состояний
            is_good = (color == self.chain_states[self.chain_prev])
        return is_good

    def _run(self, color, time):
        if not self._check_color(color):
            print(f'Неправильная последовательность переключения {self.chain_prev}->{color}')
            return False
        self.chain_prev = color
        self.__color = color
        self._shine(time)
        return True

    def _shine(self, time):
        print(self.__color, end='')
        for _ in range(time):
            sleep(1)
            print('.', end='')  # иммитация периода действия цвета
        print('')

    def running(self):
        for color, time in [('красный', 7), ('желтый', 2), ('зеленый', 5), ('зеленый', 5)]:
            if not self._run(color, time):
                print('Установлена неправильная последовательность')
                break


if __name__ == '__main__':
    light_1 = TrafficLight()
    light_1.running()
