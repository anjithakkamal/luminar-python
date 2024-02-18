# 5. Python program to check if the given number is a Disarium Number
def is_disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num
num=int(input("enter the number = "))
print("number is disarium ",is_disarium(num))