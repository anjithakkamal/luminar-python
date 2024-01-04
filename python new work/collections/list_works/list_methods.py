dishes=["vb","cb","bb","gheerost","friedrice","vb","cb"]
dishes.append("dosa")
print("using append function to add=",dishes)
#########specific position###########
dishes.insert(1,"nan")
print("inserted at aspecific position:-",dishes)
dishes.pop()
print("removed last position==",dishes)
dishes.pop(4)
print("removed specific postion==",dishes)
dishes.remove("vb")
print("remove object",dishes)
dishes.reverse()
print("reversed order:-",dishes)
dishes.sort()
print("sorted order",dishes)
print("how many cb in the list:-",dishes.count("cb"))

