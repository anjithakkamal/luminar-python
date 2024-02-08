# Q1: Write a program in python to find out LCM of two numbers
num1=int(input("enter number="))
num2=int(input("enter number="))
largest_num=max(num1,num2)
while(True):#product=num1*num2  while(product):
   if largest_num%num1==0 and largest_num%num2==0:
      lcm=largest_num
      break
   largest_num=largest_num+1
print(lcm)