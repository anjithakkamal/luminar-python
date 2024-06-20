var word="hellopython"
var wc={}
// method 1
for(let ch of word){
    ch in wc ? wc[ch]+=1:wc[ch]=1
}
console.log(wc);

// method 2
word.split("").map(ch =>ch in wc ? wc[ch]+=1:wc[ch]=1)
console.log(wc);