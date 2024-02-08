# Q3: Python program to check if the given string is a palindrome or not
# ->Palindrome-a word that reads the same backward as forward
# Madam=madaM
word="madam"
result=""
length=len(word)-1
for i in range(length,-1,-1):
    result=result+word[i]
    # print(word[i])
print(result)
print("paliandrome" if result==word else "not paliandrome")

