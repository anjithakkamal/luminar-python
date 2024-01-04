num1=int(input("enter the first number="))
num2=int(input("enter the second number="))
num3=int(input("enter the third number="))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"sorting order is {num1},{num2},{num3}")
    else:
        print(f"sorting order is {num1},{num3},{num2}")
if num2>num1 and num2>num3:
    if num1>num3:
        print(f"sorting order is {num2},{num1},{num3}")
    else:
        print(f"sorting order is{num2},{num3},{num1}")
if num3>num1 and num3>num2:
    if num1>num2:
        print(f"sorted order is{num3},{num1},{num2}")
    else:
        print(f"sorting order is{num3},{num2},{num1}")