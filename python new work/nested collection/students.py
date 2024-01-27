students=[
    {"rol":100,"name":"arjun","course":"django"},
    {"rol":101,"name":"biju","course":"mearn"},
    {"rol":102,"name":"cijoy","course":"testing"},
    {"rol":103,"name":"vipin","course":"django"},
    {"rol":104,"name":"tom","course":"mearn"},
    {"rol":105,"name":"jhon","course":"testing"},
    {"rol":106,"name":"nibin","course":"django"},
]
#print students name in the dictionary
for stud in students:
    # print(dictionary.get("name"))

#print student name whose course = django
    if stud.get("course")=="django":
        print(stud.get("name"))