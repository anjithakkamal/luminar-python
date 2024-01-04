#read three numbers num1,num2 and num3 find second largest number using if.elif
num1=int(input("enter the first number ="))
num2=int(input("enter the second number="))
num3=int(input("enter the third number="))
# if(num1<num2 and num1>num3)or(num1<num3 and num1>num2):
#     print("the second largest number is =",num1)
# elif(num2<num1 and num2>num3)or(num2<num3 and num2>num1):
#     print("the second largest number is =",num2)
# elif(num3<num1 and num3>num2)or(num3<num2 and num3>num2):
#     print("the second largest number is =",num3)
if(num1>num2)and(num1>num3):
    # 1st largest number num1
    if num2>num3:
        print(f"second largest number{num2}")
    else:
        print("second largest number",num3)
elif(num2>num1)and(num2>num3):
    # 1st largest number num2
    if num1>num3:
        print("second largest number",num1)
    else:
        print("second largest number",num3)
elif(num3>num1)and(num3>num2):
    # 1st largest number num2
    if num1>num2:
        print("second largest number",num1)
    else:
        print("second largest number",num2)
