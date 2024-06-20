var text="pneumonoultramicroscopicsilicovolcanoconiosis"
var wc={}
for(let ch of text){
    ch in wc?wc[ch]+=1:wc[ch]=1
}
var nestedArray=Object.entries(wc) 
var mostrecursive=nestedArray.reduce((w1,w2)=>w1[1]>w2[1]?w1:w2)
console.log(mostrecursive);