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

