# Write a program to count words in string 
text="luminar technolab"
wc={ch:text.count(ch) for ch in set(text)}
print(wc)
print("length of the string", len(text))

