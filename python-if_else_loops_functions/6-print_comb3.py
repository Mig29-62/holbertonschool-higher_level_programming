#!/usr/bin/python3
i = 0
j = 0
string = ''
for n in range(0, 89):
    i = n // 10   # noqa: E231,E251
    j = n % 10   # noqa: E231,E251
    if i < j:
        str = "{}{}".format(i, j)  # noqa: E251  #noqa: E231
        print(str, end=', ')  # noqa: E251,E231
    elif i == j:
        continue
    else:
        continue
print('89', end='\n')  #noqa: W292