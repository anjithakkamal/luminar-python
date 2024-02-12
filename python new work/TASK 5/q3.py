# Q3: program to merge string alternately using python
# example :
# input:"major","general"
# output: mgaejnoerral
s1=input("enter string=")
s2=input("enter string=")
length=min(len(s1),len(s2))
result=""
for i in range (0,length):
    out=s1[i]+s2[i]
    result=result+out
if len(s1)>len(s2):
    rem=s1[length:]
else:
    rem=s2[length:]
result=result+rem
print(result)
