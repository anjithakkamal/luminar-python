# Q5: program to find the number of occurrences of each vowel present in the given string
text="anjitha anithra"
print(text)
wc={}
vowels="a","e","i","o","u"
v_count=0
for t in text:
    if t in vowels:
        v_count+=1
print("vowels count :- " ,(v_count))
wc={t:text.count(t) for t in set(text)}
print(wc)