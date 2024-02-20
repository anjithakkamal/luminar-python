# 27. Write a Python program to check whether the n-th element exists in a given list.
num=int(input("enter the number = "))
list = [1, 2, 3, 4, 5]
if num in list:
    print("Element found in the list")
else:
    print("Element not found in the list.")