#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number%10
if  number < 0:
    number=number*-1
    remainder=number%10
    remainder=remainder*-1
    number=number*-1
    print(f"Last digit of {number} is {remainder} and is less than 6 and not 0") 
if  remainder == 0:
    print(f"Last digit of {number} is {remainder} and is 0") 
elif  remainder > 5:
    print(f"Last digit of {number} is {remainder} and is greater than 5") 
elif remainder < 6 & remainder != 0:
    print(f"Last digit of {number} is {remainder} and is less than 6 and not 0") 
