from re import *
text="nUm1"
rule="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(rule,text)
if matcher==None:
    print("invalid")
else:
    print("valid")