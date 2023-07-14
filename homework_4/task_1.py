# Напишите функцию для транспонирования матрицы


from copy import deepcopy


def matrix_transposition(matr):
    """Транспонирование матрицы"""

    # копирование матрицы
    result_matrix = deepcopy(matr)

    for i in range(len(matr)):
        for j in range(len(matr[0])):
            result_matrix[j][i] = matr[i][j]

    return result_matrix


matrix = [[1, 2, 5],
          [2, 7, 8],
          [87, 66, 3]]

for i in matrix:
    print(i)

trans_matrix = matrix_transposition(matrix)

print('')
for i in trans_matrix:
    print(i)
