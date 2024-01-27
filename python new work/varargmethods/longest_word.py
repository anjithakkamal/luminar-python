# text="longest word"
# words=text.split(" ")
def get_length(word):
    return len(word)
# longest_word=max(words,key=get_length)
# print("longest word is :-",longest_word)
# smallest_word=min(words,key=get_length)
# print("smallest word is :-",smallest_word)
def get_max_min_word(text,is_max=True):
    words=text.split(" ")
    if is_max==True:
        return max(words,key=get_length)
    else:
        return min(words,key=get_length)
print(get_max_min_word("longest word"))
print(get_max_min_word("longest word",is_max=False))