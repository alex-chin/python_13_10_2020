"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    def __init__(self, name, surname, position, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


company = [
    Position('Xander', 'Gibson', 'General Director', {"wage": 38224, "bonus": 4949}),
    Position('Chaney', 'Petersen', 'R&D Director ', {"wage": 23411, "bonus": 1873}),
    Position('Russell', 'Carney', 'Programmer', {"wage": 22922, "bonus": 2580})
]

for employee in company:
    print(employee.get_full_name(), employee.position, employee.get_total_income())
