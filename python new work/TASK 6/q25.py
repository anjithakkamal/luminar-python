# 25. Write a Python program to shuffle and print a specified list. 
from random import shuffle
list = [1,2,3,4,5,]
print("orginal list :- ",list)
shuffle(list)
print("shuffled list :- " , list)