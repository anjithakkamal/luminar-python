text="fat cat mat cat fat cat"
words=text.split(" ")
wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print("count of text :-",wc)