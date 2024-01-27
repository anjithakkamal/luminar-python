#keys()
course={
    "name":"django",
    "languages":"python",
    "duration":7,
    "fees":50000,
    "faculty":"sajay"
    }
for k in course.keys():
    print(k)
#values()
for v in course.values():
    print(v)
#items()
for k,v in course.items():
    print(k,v)
#get()
print("fees: ",course.get("fees"))
#update()
course.update({"duration":8,"fees":60000})
print("update fees and duration =",course)
course.pop("faculty")
print("remove faculty :",course)