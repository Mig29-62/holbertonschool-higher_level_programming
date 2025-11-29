#!/usr/bin/python3
def print_matrix_integer(a=[[]]):
    row=len(a)
    column=len(a)
    i=0
    j=0
    string=''
    while i<row:
            while j<column:
                string="{:d}".format(a[i][j])
                if j == column-1:
                    print(string,end='')
                else:
                    print(string,end=' ')
                j += 1
            print("\n")
            i += 1
            j = 0
