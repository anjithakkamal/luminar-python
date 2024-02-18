# 7. Python program to check the number of digits present in a integer 
num = 3452
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits: " + str(count))