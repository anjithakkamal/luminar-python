from unittest.mock import patch


lst=["red","green","blue","white","black","yellow"]
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\colors.txt"
fw=open(path,"w")
for c in lst:
    fw.write(c+"\n")
