#read three numbers num1,num2 and num3 find largest number using if.elif
# num1=int(input("enter the first number ="))
# num2=int(input("enter the second number ="))
# num3=int(input("enter the third number ="))
# if(num1>num2):#num1>num2 and num1>num3
#     print("the largest number is =",num1)
# elif(num2>num3): #num2>num1 and num2>num3
#     print("the largest number is =",num2)
# else: #num3>num1 and num3>num2
#     print("the largest number is =",num3)

# if(num1>num2 and num1>num3):
num1=int(input("enter the first number ="))
num2=int(input("enter the second number ="))
num3=int(input("enter the third number ="))
if(num1>num2 and num1>num3):
    print("num 1 is the largest number")
if(num2>num1 and num2>num3):
    print("num2 is the largest number")
if(num3>num1 and num3>num2):
    print("num3 is the largest number")