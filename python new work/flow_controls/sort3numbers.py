#read three numbers num1,num2 and num3 sort these three number using if.elif
print("----PRINT THREE NUMBERS IN SORTING ORDER------")
num1=int(input("enter the first number ="))
num2=int(input("enter the second number ="))
num3=int(input("enter the third number ="))
if(num1>num2>num3):
    print("sorting order is =",num3,num2,num1)
elif(num1>num3>num2):
    print("sorting order is =",num2,num3,num1)
elif(num2>num3>num1):
    print("sorting order is =", num1,num3,num2)
elif(num3>num2>num1):
    print("sorting order is =",num1,num2,num3)
elif(num3>num1>num2):
    print("sorting order is =",num2,num1,num3)
elif(num2>num1>num3):
    print("sorting order is =",num3,num1,num2)