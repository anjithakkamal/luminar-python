#24 Write a Python program to print the numbers of a specified list after removing even numbers from it. 
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print("list :- " , num)
num1 = [x for x in num if x % 2 != 0]
print("after removing even numbers:- " ,num1)
