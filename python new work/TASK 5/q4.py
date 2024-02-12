# Q4: program to sort characters of the strings, first symbol followed by digits
# example:
# input: a2b4c6
# output: abc246
string="a2b4c6"
print("orginal string :- " ,string)
alpha=[]
digit=[]
for t in string:
    if t.isalpha():
        alpha.append(t)
    else:
        digit.append(t)
result="".join(alpha+digit)
print("sorted string :- ",result)



