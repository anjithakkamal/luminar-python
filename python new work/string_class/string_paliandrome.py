word="malayalam"
result=""
length=len(word)-1
for i in range(length,-1,-1):
    result=result+word[i]
    # print(word[i])
print(result)
print("paliandrome" if result==word else "not paliandrome")
