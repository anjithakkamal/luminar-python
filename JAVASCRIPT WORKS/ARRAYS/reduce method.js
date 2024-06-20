var arr=[10,11,12,13,14,15,16]
// total
var total=arr.reduce((n1,n2)=>n1+n2)
console.log(`total ${total}`);

// product
var product=arr.reduce((n1,n2)=>n1*n2)
console.log(`product ${product}`);

// maximum
var max=arr.reduce((n1,n2)=>n1>n2?n1:n2)
console.log(`max ${max}`);

// minimum
var min=arr.reduce((n1,n2)=>n1<n2?n1:n2)
console.log(`min ${min}`);