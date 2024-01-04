num1=int(input("enter num1="))
num2=int(input("enter num2="))
op=input("operator")
if op=="+":
    result=num1+num2
    print(f"result{num1}+{num2}={result}")
elif op=="-":
    result=num1-num2
    print(f"result{num1}-{num2}={result}")
elif op=="*":
    result=num1*num2
    print(f"result{num1}*{num2}={result}")
elif op=="/":
    result=num1/num2
    print(f"result{num1}/{num2}={result}")
else:
    print("enter valid operator")