#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    for i in range(0,length-1):
        if ord(my_string[i]) == 67:
            new_string = my_string[:i] + my_string[i + 1:]
        if ord(my_string[i]) == 99:
            new_string=my_string[:i]+my_string[i+1:]


    return new_string