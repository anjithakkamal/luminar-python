numbers=[1,2,3,4,5,6,7,8,9,10]
odd_list=[]
even_list=[]
for num in numbers:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("even list",even_list)
print("odd list",odd_list)