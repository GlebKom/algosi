def matrix_trans(matrix):
    trans_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(trans_matrix)):
        for j in range(len(trans_matrix[0])):
            trans_matrix[i][j] = matrix[j][i]
    return trans_matrix

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = sum(matrix1[i][n] * matrix2[n][j] for n in range(len(matrix2)))
        return result
    else:
        return 'Матрицы несовместимы.'

def matrix_input():
    matrix = []
    while True:
        line = input('Введите строку матрицы(числа вводите через пробел, для окончания ввода нажмите Enter без ввода): ')
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


def rank(matrix):
    matrix_copy = matrix.copy()
    for row in matrix_copy:
        if row.count(0) == len(row):
            matrix.remove(row)

    for r in range(len(matrix)):
        div = False
        for i in range(len(matrix[r])):
            if matrix[r][i] != 0:
                div = matrix[r][i]
                break
        if div:
            for q in range(len(matrix[r])):
                matrix[r][q] = matrix[r][q] / div

            for p in range(r + 1, len(matrix)):
                k = matrix[p][i] / matrix[r][i]
                for n in range(len(matrix[p])):
                    matrix[p][n] = matrix[p][n] - k * matrix[r][n]
    matrix_rank = len(matrix)

    for row in matrix:
        if row.count(0) == len(row):
            matrix_rank = matrix_rank - 1
    return matrix_rank

def interface():
    wtd = input('Введите какую операцию вы хотите выполнить(умножение, транспонирование, ранг): ')
    if wtd == 'транспонирование' or wtd == 'Транспонирование':
        matrix = matrix_input()
        if matrix:
            return matrix_trans(matrix)
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
            return matrix_multiplication(matrix1, matrix2)
        else:
            return 'Неправильный формат ввода матриц.'

    elif wtd == 'ранг' or wtd == 'Ранг':
        print('Введите матрицу.')
        matrix = matrix_input()
        if matrix:
            return 'Ранг равен: ' + str(rank(matrix)) + '.'
        else:
            return 'Неправильный формат ввода данных.'

    else:
        return 'Проверьте правильность написания операции.'

print(interface())
