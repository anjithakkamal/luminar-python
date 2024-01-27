from importlib.resources import path


vehicle_number=["kl-05-jk-6479","ka-05-hj-8128","tn-09-ty-6567","kl-08-hj-9999"]
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\vehicle_number.txt"
f=open(path,"w")
for number in vehicle_number:
    if number.startswith("kl"):
        f.write(number+"\n")
