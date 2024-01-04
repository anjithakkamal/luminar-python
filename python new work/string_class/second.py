text="i have 2 cycle 3 bike 1 car"
#print numbers
words=text.split(" ")
for w in words:
    if w.isdigit():
        print(w)