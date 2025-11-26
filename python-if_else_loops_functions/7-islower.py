from operator import truediv
from selectors import SelectSelector


def islower(c):
    c=ord(c)
    if c >= 97 & c <= 122 :
        return True
    else:
        return False
