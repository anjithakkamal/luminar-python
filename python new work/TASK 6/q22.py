# 22. Write a Python program to multiply all the items in a list. 
def mul_list(list) :
    product = 1
    for i in list:
         product = product * i
    return product
my_list = [1,2,3,4,5]
print("my list is :- " ,my_list)
print("product of alist is :- " ,mul_list(my_list))