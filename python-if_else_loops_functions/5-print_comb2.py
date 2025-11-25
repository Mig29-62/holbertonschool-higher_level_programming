#!/usr/bin/python3
i = 0
j = 0
string = ''
for n in range(0, 99):
    i = n // 10   # noqa: E231,E251
    j = n % 10   # noqa: E231,E251
    str = "{}{},".format(i,j)   # noqa: E251,E231
    print(str, end=' ')   # noqa: E251,E231
print('99', end='\n')
