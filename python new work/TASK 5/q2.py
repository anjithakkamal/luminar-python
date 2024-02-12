# Q2: write a program in python to print the characters present at even index and odd index 
# separately for the given string
string="luminar"
even=[]
odd=[]
for i in string:
    if string.index(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even characters :- " ,even)
print("odd characters :- ",odd)



