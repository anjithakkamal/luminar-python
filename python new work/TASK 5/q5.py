# Q5: program to find the number of occurrences of each vowel present in the given string
text="luminar technolab"
print(text)
vowels="a","e","i","o","u"
v_count=0
for t in text:
    if t in vowels:
        v_count+=1
print("vowels count :- " ,v_count)