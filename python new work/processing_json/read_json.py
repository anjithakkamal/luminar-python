from json import load
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\processing_json\\students.json"
f=open(path,"r")
data=load(f)
for dictionary in data:
    print(dictionary.get("name"))
    print(dictionary.get("course"))

# for dictionary in data:
#     if dictionary.get("place")=="thrissur":
#         print("thrissur students",dictionary.get("name"))

place_filter=[dictionary.get("name") for dictionary in data if dictionary.get("place")=="thrissur"]
print(place_filter)
all_course=[dictionary.get("course") for dictionary in data]
print("course",set(all_course))

st=set()
for dictionary in data:
    course=dictionary.get("course")
    st.add(course)
print(st)