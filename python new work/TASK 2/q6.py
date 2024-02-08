# Q6: Python program to check given number is prime or not
num=int(input("enter number="))
is_prime=True
if num==1:
    is_prime=False
# elif num==2:
#     is_prime=True
else:
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
print(is_prime)