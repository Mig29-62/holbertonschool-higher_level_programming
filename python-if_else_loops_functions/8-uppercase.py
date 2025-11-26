#!/usr/bin/python3
def uppercase(str):
    string2=''
    length=len(str)
    for i in range(0,length):
        c=ord(str[i])
        c=c-32
        string2=string2+chr(c)
    print("{}".format(string2),end='\n')