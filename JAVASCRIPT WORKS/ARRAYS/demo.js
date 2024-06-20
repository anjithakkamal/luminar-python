var expenses=[10000,20000,14000]
//              0     1     2
console.log(expenses[2]);   //op=140000


// ====================array iteration==============method1
for(let i=0;i<expenses.length;i++){
    console.log(expenses[i]);
}

// ===========================array iteration======method 2
for(let exp of expenses){
    console.log(exp);
}
// ==============expense update first 23000
var expenses=[10000,20000,14000]
expenses[0]=23000
console.log(expenses);


