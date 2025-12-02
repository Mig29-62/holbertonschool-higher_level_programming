#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    addition=0
    prev=0
    length=len(roman_string)
    for element in reversed(roman_string):
        if roman_dict[element] < prev:
            addition -= roman_dict[element]
        elif roman_dict[element] > prev:
            addition += roman_dict[element]
        else:
            addition += roman_dict[element]
        prev=roman_dict[element]
    return addition