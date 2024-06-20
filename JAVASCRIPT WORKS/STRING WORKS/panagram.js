var text="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG".toLowerCase()

var aplhabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ".toLowerCase()

var isPanagram=true

for(let ch of aplhabets){

    if(!text.includes(ch)){

        isPanagram=false

        break
    }
}
console.log(isPanagram);