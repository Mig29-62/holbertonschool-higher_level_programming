#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    length_2=len(matrix[0])
    for i in range(length-1):
        for j in range(length_2-1):
            matrix[i][j]=matrix[i][j]**2
    return matrix