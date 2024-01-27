path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\years.txt"
f=open(path,"w")
for y in range(1800,2025):
    f.write(str(y)+"\n")