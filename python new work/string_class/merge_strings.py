str1="abcdefgh"
str2="pqrst"
length=len(str1)
output=""
for i in range(0,length):
    # print(str1[i],str2[i])
    output=output+str1[i]+str2[i]
    # output+=str1[i]+str2[i]
rem=str2[length:]
output=output+rem#output+=rem
print(output)