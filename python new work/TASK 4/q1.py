# Q1:  Write a program to print the pattern given below
# *
# * *
# * * *
# * * * *
# * * * * *
for row in range(1,6):
    for col in range(1,row+1):
        print("*",end="\t")
    print()