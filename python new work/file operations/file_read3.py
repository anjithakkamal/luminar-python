path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\story.txt"
f=open(path,"r")
all_words=[]
for line in f:
    cleaned_string=line.strip("\n")
    words=cleaned_string.split(" ")
    for w in words:
        all_words.append(w)
print("all words =",all_words)
wc={w:all_words.count(w) for w in set(all_words)}
print("count of all words in the story text file",wc)