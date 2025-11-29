#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row=len(matrix)
    column=len(matrix[0])
    i=0
    j=0
    string=''
    while i<row:
            while j<column:
                string="{:d}".format(a[i][j])
                print(string,end=' ')
                j += 1
            print("\n")
            i += 1
