def unique_string(text):
    common_chars=[]
    for char in text:
        if char not in common_chars:
            common_chars.append(char)
    return("").join(common_chars)
print(unique_string("helloworld"))

#longest sub string