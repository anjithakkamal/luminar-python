# 15 Python program to print the smallest element in an array 
arr=[25,77,56,99,18,11]
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
print("Smallest element in the array ", min)