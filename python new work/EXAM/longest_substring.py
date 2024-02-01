
text="acacdaad"
# text="racecar"
#     01234567
paliandrome_list=[]
for i in range(len(text)):
    # p,n=i,i
    
    p=i
    n=i
    # while(p>=0 and n<len(text)
    while(p>=0 and n<len(text) and text[p]==text[n]):
        paliandrome_text=text[p:n+1]
        paliandrome_list.append(paliandrome_text)
        p-=1
        n+=1
    p=i
    n=i+1
    while(p>=0 and n<len(text) and text[p]==text[n]):
        paliandrome_text=text[p:n+1]
        paliandrome_list.append(paliandrome_text)
        p-=1
        n+=1

print(paliandrome_list)
# longest_palindrome=max(paliandrome_list)
# print(longest_palindrome)
def get_length(w):
    return len(w)
print(max(paliandrome_list,key=get_length))