# 28. Write a Python function to find the maximum of three numbers. 
def find_max(a, b, c):
    if (a >= b) and (a >= c): 
        return a
    elif (b >= a) and (b >= c): 
        return b
    else:
        return c
print("maximum of three number is in 10,2,30:-" ,find_max(10,2,30))