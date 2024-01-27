source_word="container"
target_word="can"
wc={ch:source_word.count(ch) for ch in set(source_word)}
print(wc)
for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        print("not a kangaroo word")
        break
else:
    print("kangaroo word")