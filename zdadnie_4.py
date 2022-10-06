import copy
import numpy as np
import timeit

matrix = [[2, -1, 4], [7, 2, 3], [3, -2, 1]]
def det(matrix):
    d = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1]*matrix[1][2]*matrix[2][0]) + \
        (matrix[1][0] * matrix[2][1] * matrix[0][2]) - (matrix[0][2]*matrix[1][1]*matrix[2][0]) - \
        (matrix[1][0] * matrix[0][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1] * matrix[0][0])
    return d

def minor(i, j, matrix):
    matrix_copy = copy.deepcopy(matrix)
    matrix_copy.pop(i)
    for q in range(len(matrix_copy)):
        matrix_copy[q].pop(j)
    return (-1)**(i + j) * (matrix_copy[0][0] * matrix_copy[1][1] - matrix_copy[0][1] * matrix_copy[1][0])

def matrix_reverse(matrix):
    d = det(matrix)
    reversed_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            reversed_matrix[j][i] = minor(i, j, matrix) / d
    return reversed_matrix

start_time = timeit.default_timer()
matrix_reverse(matrix)
time1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
np.linalg.inv(matrix)
time2 = timeit.default_timer() - start_time

print(time1)
print(time2)

