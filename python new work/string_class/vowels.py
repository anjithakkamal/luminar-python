text="pneumonoultramicroscopi@#csilicovolcan$oconiosis"
print("----pneumonoultramicroscopicsilicovolcanoconiosis------")
#a)print total number of characters
# print("print total number of characters=",text.count(""))
#b) total number of vowels
#c) total number of consonants

vowels=("a","e","i","o","u")
v_count=0
c_count=0
char_count=0
for ch in text:
    if ch.isalpha():
        char_count+=1
for ch in text:
    if ch in vowels:
        v_count+=1
    else:
        c_count+=1
print("total number of vowels",v_count)
print("total number of consonants",c_count)
print("total number of characters",len(text))
print("character count",char_count)#not include@,#,*,&etc
