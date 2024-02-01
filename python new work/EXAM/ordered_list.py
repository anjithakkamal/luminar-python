text="aabcc"
lst=[]
[lst.append(ch) for ch in text if ch not in lst]
print(lst)