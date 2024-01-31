#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix
        return None

    for row in matrix:
        for index, element in enumerate(row):
                square = element**2
                print("{:d}".format(square))
