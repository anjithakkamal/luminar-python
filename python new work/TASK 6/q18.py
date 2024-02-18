# 18. Python Program to Find Armstrong Number in an Interval 
for num in range(1,401):
     order = len(str(num))
     sum = 0
     temp = num
     while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       if num == sum:
           print(num)