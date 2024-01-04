ben_liked_colors=["yellow","white","green","red"]
shyam_liked_colors=ben_liked_colors.copy()#using copy shyam use another m/y location
print(shyam_liked_colors is ben_liked_colors)
shyam_liked_colors=ben_liked_colors
print(shyam_liked_colors is ben_liked_colors)
