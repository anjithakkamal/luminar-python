path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\colors.txt"
f=open(path,"r")
colors_list=[]
for line in f:
    colors_list.append(line.rstrip("\n"))
print("colors list =",colors_list)
print("using set remove duplicate =",set(colors_list))