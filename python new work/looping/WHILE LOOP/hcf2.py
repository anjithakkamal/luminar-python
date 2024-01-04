num1=int(input("enter number="))
num2=int(input("enter number="))
smallest_no=num1 if num1<num2 else num2
i=1
hcf=1
while(i<=smallest_no):
    if(num1%i==0) and(num2%i==0):
        hcf=i
    i=i+1
print(f"hcf of {num1},{num2}={hcf}")