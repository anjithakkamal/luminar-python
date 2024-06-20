class Student{

    constructor(name,course,degree){
        this.name=name;
        this.course=course;
        this.degree=degree
    }
    printStudent(){
        console.log(this.name,this.course,this.degree);
    }
}

var obj=new Student("anji","python","mca");
obj.printStudent()