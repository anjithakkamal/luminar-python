var colors=["red","green","yellow","blue"]
var colorscopy=[...colors]    //...spreadoperator
colorscopy.pop()
console.log(colors);
console.log(colorscopy);

var user={name:"hari",email:"har@gmail.com",password:"Pasword@123",isActive:true}
var usercopy={...user}
usercopy.isActive=false
console.log(user);
console.table(usercopy)

var product={id:1,name:"m32",brand:"samsung",price:12000,isAvailable:false}
var productcopy={...product,isAvailable:true}
console.log(productcopy);