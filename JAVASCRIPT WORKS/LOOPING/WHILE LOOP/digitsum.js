var num=153
var sum=0
while (num!=0){
    digit=num%10
    sum=sum+digit
    num=Math.floor(num/10)
}
console.log(sum);