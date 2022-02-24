# task_10_1.py
# Задание 1
# Реализовать класс Matrix (матрица).
#
# - Обеспечить перегрузку конструктора класса(метод __init__()), который
#   должен принимать данные(список списков) для формирования матрицы.В случае
#   если список списков некорректный - возбуждать исключение ValueError
#   с сообщением fail initialization matrix.
#
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
#
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 43 |
# | 22 51 |
# | 37 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 - 8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# - Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
#   в привычном виде(как показано выше).
# - Далее реализовать перегрузку метода __add__() для сложения двух объектов
#   класса Matrix(двух матриц).Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и пр.
#
import copy
from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        try:
            self.is_matrix = False
            columns = 0
            for row in range(len(matrix)):
                row_columns = len(matrix[row])
                for i in matrix[row]:
                    b_int = isinstance(i, int)
                    if b_int is False:
                        raise ValueError('ValueError')
                if not columns:
                    columns = row_columns
                elif columns == row_columns:
                    self.is_matrix = True
                else:
                    self.is_matrix = False
                    break
            if self.is_matrix:
                self.__matrix = matrix
            else:
                raise ValueError('ValueError')
        except ValueError as error:
            print(f"{error}: fail initialization matrix")

    def __str__(self):
        result_str = ""
        for row in range(len(self.__matrix)):
            matrix_str = "| "
            for col in range(len(self.__matrix[row])):
                matrix_str = matrix_str + f"{(self.__matrix[row][col])} "
            matrix_str = matrix_str + "|\n"
            result_str = result_str + matrix_str
        return result_str

    def __add__(self, other):
        a = self.__matrix
        b = other.__matrix        
        rows = len(a)
        cols = len(a[0])
        result = [[0] * cols for _ in range(rows)]
        for row in range(len(result)):
            for col in range(len(result[row])):
                result[row][col] = a[row][col] + b[row][col]
        return Matrix(result)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    # """
    # | 1 2 |
    # | 3 4 |
    # | 5 6 |
    print(second_matrix)
    # """
    # | 6 5 |
    # | 4 3 |
    # | 2 1 |
    # """
    print(first_matrix + second_matrix)
    # """
    # | 7 7 |
    # | 7 7 |
    # | 7 7 |
    # """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    # """
    # Traceback (most recent call last):
    #   ...
    # ValueError: fail initialization matrix
    # """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    fail_matrix_2 = Matrix([['abc', 2], [3, 4], [5, 6]])
