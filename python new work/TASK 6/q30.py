# 30. Write a Python program to reverse the order of the items in the array. 
arr = [1, 2, 3, 4, 5];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
print("Array in reverse order: ");    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i]),     