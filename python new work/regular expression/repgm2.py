from itertools import count
from re import *
text="Pam has a cat. The cat is fat. The fat cat is black. Black fat cat sat in the jam. Pam has a rag bag. In the bag went Black Fat Cat. Dad and Pam ran with Black Fat Cat to the tap."
pattern="am"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"Total count pattern {pattern}={count}")