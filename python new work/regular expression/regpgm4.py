from re import *
text="fatboy @2KB2"                        # to take integers
# pattern="\d"      [0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="\D"                                [^0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())            # excluding integers [a-zA-z]


# pattern="\w"                                #alphanumeric      [a-zA-Z0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())  


# pattern="\W"                                #special charaters     [^a-zA-Z0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())  

pattern="\s"                                #space     
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())  


pattern="\S"                                #space
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())  