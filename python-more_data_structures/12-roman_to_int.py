#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    addition=0
    for letter in roman_string:
        if roman_dict[letter+1] > roman_dict[letter]:
            addition -= roman_dict[letter]
        else:
            addition += roman_dict[letter]
    return addition