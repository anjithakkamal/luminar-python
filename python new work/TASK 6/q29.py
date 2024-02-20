# 29. Write a Python function that accepts a string and counts the number of upper- and lower-case letters
def lowerupper(string):
    upper=0
    lower=0
    for ch in string:
        if ch.islower():
            lower+=1
        else:
            upper+=1
    return lower,upper
string="Luminar TEchnolab"
l,u=lowerupper(string)
print("string :- ",string)
print("lowercase letters count :- ",l)
print("uppercase letters count :- " ,u)

