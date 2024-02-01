from itertools import count


def count_vowels(txt):
    text=txt.casefold()
    count=0
    vowels=("a","e","i","o","u")
    for ch in text:
        if ch in vowels:
            count=count+1
    return count
txt="The quick brown fox jumps over the lazy dog"
print(count_vowels(txt))