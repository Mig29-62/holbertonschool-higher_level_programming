#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    addition=0
    for letter in roman_string:
        pos=roman_string.find(letter)
        if len(roman_string) == 1:
            addition += roman_dict[letter]
        elif roman_string[pos+1] > roman_string[pos]:
            addition -= roman_dict[letter]
        else:
            addition += roman_dict[letter]
    return addition