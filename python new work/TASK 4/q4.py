# Q4:  Write a Python program to create the multiplication table (from 1 to 10) of a number.
num=6
print("----MULTIPLICATION TABLE OF SIX-----")
for i in range(1,11):
    mul=num*i
    print(i,"*",num,"=",mul)
    i=i+1