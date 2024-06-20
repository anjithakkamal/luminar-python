var students={
    name:"Anjitha",      //property:"value"
    course:"django",
    degree:"mca",
    total:450,
    points:10
}
console.log(students.name);
console.log(students.course);
students.grade="A+"
console.log(students);
if ("total" in students){    //total property checking
    console.log("present");
}
else{
    console.log("not present");
}
//if point exist add 10 extra 

if("points" in students){
    students.points+=10   //update
}
else{ //add
    students.points=15
}  
console.log(students);