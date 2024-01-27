list=[100,200,300,150]
max1=list[0]
max2=list[0]
for num in list:
    if num>max1:
        max2=max1
        max1=num
    elif num>max2:
        max2=num
# max_sum=max1+max2
print("max pairs are =",max1,max2)
# print("max pair sum =",max_sum)
