# quantifiers(*,+,?,{})

from re import *
text="aabaaabcaabccaaaa"
# pattern="a*"                          #chck for any number of a including zero
# pattern="a{2}"                        #chck 2 a
pattern="a{2,3}"                        #minimum2 maximum3
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())