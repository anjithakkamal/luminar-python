text="this is a goodmorning message"
#print longest word in the string
word=text.split(" ")
print(word)
def get_len(w):
    return len(w)
max_word=max(word,key=get_len)
print("longest word in the text is:",max_word)
min_word=min(word,key=get_len)
print("shortest word in the text is:",min_word)
srt_words=sorted(word,key=get_len,reverse=True)
print("sorted order",srt_words)