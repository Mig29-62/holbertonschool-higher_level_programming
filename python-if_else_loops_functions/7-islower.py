#!/usr/bin/python3
def islower(str):
    string2=''
    length=len(str)
    for i in range(0,len):
        c=ord(str[i])
        c=c-32
        string2=string2+chr(c)
    print(string2)