var arr=[10,20,30,40,50]

var k=2

for(i=0;i<k;i++){

    let pop_element=arr.pop()

    arr.unshift(pop_element)

}
console.log(arr);