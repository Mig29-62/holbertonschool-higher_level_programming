#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    length = len(new_matrix)
    length_2=len(new_matrix[0])
    for i in range(length):
        for j in range(length_2):
            new_matrix[i][j]=new_matrix[i][j]**2
    return new_matrix