phone_number=["9947374509","9495444621","9048474509","98954543","8904xxx456","78787"]
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\phonenumber.txt"
f=open(path,"w")
for number in phone_number:
    if len(number)==10 and number.isdigit():
        f.write(number+"\n")
        
    