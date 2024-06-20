var text="hello hai hello hai hello hello"
wc={}
var words=text.split(" ");
console.log(words);
for(let ch of words){
    if(ch in wc){
        wc[ch]+=1
    }
    else{
        wc[ch]=1
    }
}
console.log(wc);
////////////
text.split(" ").map(w => w in wc ? wc[w]+=1 : wc[w]=1)
console.log(wc);
