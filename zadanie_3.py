import numpy as np
from numpy import linalg as LA
import timeit

def matrix_input():
    matrix = []
    while True:
        line = input(
            'Введите строку матрицы(числа вводите через пробел, для окончания ввода нажмите Enter без ввода): ')
        if not line:
            break
        try:
            line1 = list(map(int, line.split()))
            matrix.append(line1)
        except ValueError:
            return False

    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            return False
            break
    return matrix

def interface():
    wtd = input('Введите какую операцию вы хотите выполнить(умножение, транспонирование, ранг): ')
    if wtd == 'транспонирование' or wtd == 'Транспонирование':
        matrix = matrix_input()
        if matrix:
            return matrix.transpose()
        else:
            return 'Неправильный формат ввода матрицы.'

    elif wtd == 'умножение' or wtd == 'Умножение':
        print('Введите первую матрицу.')
        matrix1 = matrix_input()
        if not matrix1:
            return 'Неправильный формат ввода матриц.'
        print('Введите вторую матрицу.')
        matrix2 = matrix_input()
        if matrix1 and matrix2:
            return np.dot(matrix1, matrix2)
        else:
            return 'Неправильный формат ввода матриц.'

    elif wtd == 'ранг' or wtd == 'Ранг':
        print('Введите матрицу.')
        matrix = matrix_input()
        if matrix:
            return 'Ранг равен: ' + str(LA.matrix_rank(matrix)) + '.'
        else:
            return 'Неправильный формат ввода данных.'

    else:
        return 'Проверьте правильность написания операции.'
print(interface())