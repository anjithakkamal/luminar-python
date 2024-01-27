numbers=[0,1,0,1,0,1]
wc={}
for num in numbers:
    if num in wc:
        wc[num]+=1
    else:
        wc[num]=1
print("number count in the list :-",wc)