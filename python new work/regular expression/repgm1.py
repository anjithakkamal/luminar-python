from itertools import count
from re import *
text="fat cat run very fast to catch"
pattern="at"
count=0
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
    count+=1
print("total occurance of at ",count)