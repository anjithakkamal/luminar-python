#def is_armstrong (num) return true if num is armstrong else return false
from ast import Num
from unicodedata import digit


def is_armstrong(num):
    digit_count=len(str(num))
    orginal=num
    result=0
    while(num!=0):
        digit=num%10
        exp=digit**digit_count
        result=result+exp
        num=num//10
    if orginal==result:
        return True
    else:
        return False
print(is_armstrong(150))