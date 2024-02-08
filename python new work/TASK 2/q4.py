# Q4: Python program to check if a given number is an Armstrong number  
# ->An Armstrong number is a number that equals to the sum of its individual,digits each raised to the power of the number of digits
# eg:- 153
# number of digits  = 3
# 1^3+5^3+3^3=1+125+27=153
num=input("enter number=")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
print(sum)
if(original==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")

