"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных. """


class MyDate:
    _year = 0
    _month = 0
    _day = 0

    def __init__(self, str_date: str):
        """
        принимает дату в виде строки формата «день-месяц-год».
        :param str_date:
        """
        self.build_date(str_date)

    @classmethod
    def set_date(cls, str_date: str):
        return cls(str_date)

    @staticmethod
    def check_date(date=0, month=0, year=0):
        is_ok = False
        if date and 1 <= date <= 31:
            is_ok = True
        if month and 1 <= month <= 12:
            is_ok = True
        if year and 1970 <= year <= 2060:
            is_ok = True
        return is_ok

    def build_date(self, str_date):
        #  принимает дату в виде строки формата «день-месяц-год».
        self._day, self._month, self._year = tuple(map(int, str_date.split('-')))
