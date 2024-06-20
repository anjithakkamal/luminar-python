// armstrong number
var num=1634
var sum=0
var orginal=num
var number_count=String(num).length
while(num!=0){
    digit=num%10
    cube=digit**number_count
    sum=sum+cube
    num=Math.floor(num/10)
}
console.log(sum);
console.log(orginal==sum?"armstrong":"not armstrong");