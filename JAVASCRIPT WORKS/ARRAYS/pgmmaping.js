var arr=[12,13,14,15]
// print squres of all numbers
function squares(num){
    return num**2
}
var squ=arr.map(squares)
console.log(squ);



// 6)cubes using map method
var arr=[10,20,30,40,22]
var cubes=arr.map(num=>num**3)
console.log(cubes);

// 7)squares using map method
var squares=arr.map(num=>num**2)
console.log(squares);

// 8) if num<12 num-1
//    if num>12 num+1

var arr=[10,20,11,40,12,22]
var result=arr.map(num=>num>12?num+1:num<12?num-1:num)
console.log(result);