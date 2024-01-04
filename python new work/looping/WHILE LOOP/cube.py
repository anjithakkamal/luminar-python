#num=151 output become=5**3 + 4**3 + 3**3
num=151
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit**3
    num=num//10
print(sum)
