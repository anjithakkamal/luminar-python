#  6. Python program to determine whether the given number is a Harshad Number 
num = int(input("enter the number = "))    
rem = 0
sum = 0;       
n = num;    
while(num > 0):    
    rem = num%10;    
    sum = sum + rem;    
    num = num//10;        
if(n%sum == 0):    
    print(str(n) + " is a harshad number");    
else:    
    print(str(n) + " is not a harshad number");    