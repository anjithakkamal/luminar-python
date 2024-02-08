# Q2: Python program to calculate the sum of the odd numbers within the given range
i=10
sum=0
while(i<=50):
    if(i%2!=0):
        sum=sum+i
    i=i+1
print("sum of all even numbers from 10 to 50 =",sum)
