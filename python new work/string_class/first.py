# tweets="this is a sampletweet @stocks @sachin @rahul mentioned"
# #(1)extract words
# words=tweets.split(" ")#op:['this', 'is', 'a', 'sampletweet', '@stocks', '@sachin', '@rahul', 'mentioned']
# print(words)
# for w in words:
#     if w.startswith("@"):
#         print(w)
text="#orange color wow #yelow color wow #blue color wow"
words=text.split(" ")
# print(words)
for w in words:
    if w.startswith("#"):
        print(w.lstrip("#"))
