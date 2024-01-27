#world cup winners team
#team:world cup count
#highest world cup winners
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\worldcup.txt"
f=open(path,"r")
teams=[]
for line in f:
    data=line.rstrip("\n").split(" ")
    teams.append(data[1])
print("world cup winners teams :- ",set(teams))
wc={t:teams.count(t) for t in set(teams)}
print("world cup team count :- ",wc)
value_key_list=[(v,k) for k,v in wc.items()]
print("highest winners :- ",max(value_key_list))
