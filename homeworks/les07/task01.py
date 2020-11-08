"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых
математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """
import itertools


class Matrix:
    data = [[]]  # матрица как список строк

    def __init__(self, matrix_row_col):
        self.data = matrix_row_col

    def __str__(self):

        buf = ''
        pos = len(str(max(itertools.chain(*self.data)))) + 1
        for row in self.data:
            for el in row:
                buf += f'{el:{pos}}'
            buf += '\n'
        return buf

    def __add__(self, other):
        r_list = []
        for r_idx in range(len(self.data)):
            c_list = []
            for c_idx in range(len(self.data[0])):
                c_list.append(self.data[r_idx][c_idx] + other.data[r_idx][c_idx])
            r_list.append(c_list)
        return Matrix(r_list)


if __name__ == '__main__':
    m = Matrix([[145, 2, 3], [4, 665, 6]])
    print(m)
    m1 = Matrix([[10, 20], [23333, 90]])
    print(m1)
    m2 = Matrix([[10, 200], [30, 24]])
    print(m2)
    m3 = m1 + m2
    print(m3)
