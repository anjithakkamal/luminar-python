#word count method 2
text="goodmorning"
set_text=set(text)
wc={}
for ch in set_text:
    wc[ch]=text.count(ch)
print(wc)
#dictionary comprehesion
text="goodmorning"
wc={ch:text.count(ch) for ch in set(text)}
print(wc)