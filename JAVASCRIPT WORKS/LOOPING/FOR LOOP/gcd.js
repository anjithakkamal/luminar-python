var num1=30
var num2=45
var gcd=1
var smallest=num1<num2?num1:num2
for(let i=1;i<=smallest;i++){
    if(num1%1==0 && num2%i==0){
        gcd=i
    }
}
console.log(gcd);