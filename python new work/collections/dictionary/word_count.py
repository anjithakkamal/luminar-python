text="thiruvananthapuram"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print("word count of text is :-",wc)

