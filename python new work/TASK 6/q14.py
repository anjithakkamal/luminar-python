# Python program to print the largest element in an array 
arr=[25,77,56,99,1,11]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("largest element in the array ", max)