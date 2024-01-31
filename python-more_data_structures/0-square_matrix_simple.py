#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            square = matrix[i][j]**2
            print(matrix[i][j], end=' ')
