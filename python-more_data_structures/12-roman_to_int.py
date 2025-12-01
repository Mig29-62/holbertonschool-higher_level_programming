def roman_to_int(roman_string):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    addition=0
    for letter in roman_string:
        addition += roman_dict[letter]
    return addition