#!/usr/bin/python3
i = 1
str = ''
while i < 99:
    str = hex(i)+''
    print("{}={}".format(i,str), end='\n')
    i = i + 1
