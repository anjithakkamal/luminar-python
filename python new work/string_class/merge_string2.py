string1=input("enter string=")
string2=input("enter string=")
len_str1=len(string1)
len_str2=len(string2)
smallest_length=len_str1 if len_str1<len_str2 else len_str2
output=""
for i in range(0,smallest_length):
    output=output+string1[i]+string2[i]
if len(string1)>len(string2):
    rem=string1[smallest_length:]
else:
    rem=string2[smallest_length:]
output=output+rem
print(output)
    
# max_word=max(smallest_string,key=get_len)
