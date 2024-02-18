# 2. Python Program to Find HCF 
num1=12
num2=24
hcf=1
i=1
while(i<=num1):
    if(num1%i==0) and(num2%i==0):
        hcf=i
    i=i+1
print(f"hcf of {num1},{num2}={hcf}")