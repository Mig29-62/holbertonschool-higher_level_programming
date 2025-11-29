#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in matrix[0]:
            matrix[row][col]=matrix[row][col]**2
    return matrix