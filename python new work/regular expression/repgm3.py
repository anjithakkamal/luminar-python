
from re import *
text="anj I2th& 3ak"
# pattern="[a-z]"                      #check all lowercase alphabets       [a-zA-Z]character set      
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="[A-Z]"                      #check all uppercase alphabets
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# pattern="[a-zA-Z]"                   #check all lowercase and uppercase alphabets
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="[0-9]"                   #check all digit
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="[a-zA-Z0-9]"                   #check all alphanumeric
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="[^a-zA-Z0-9]"                    #excluding alphanumeric
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

pattern="[abc]"                              #either a,b,c
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())