#!/usr/bin/python3
i = 0
j = 0
string=''
for n in range(0,100):
    i=n/10
    i=n%10
    str="{}{}".format(i,j)
    print(str)
print('\n')
