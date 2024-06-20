var arr=["program","project","profile","profession","python","django"]

// conert to uppercase
var UpperCaseString=arr.map(w=>w.toUpperCase())
console.log(UpperCaseString);

// print length of all string
var lengthofstring=arr.map(w=>w.length)
console.log(lengthofstring);

// return words starting with "pro"
var prostrtswith=arr.filter(w=>w.startsWith("pro"))
console.log(prostrtswith);

// longest word
var longestword=arr.reduce((w1,w2)=>w1.length>w2.length?w1:w2)
console.log(longestword);

// shortest word
var shortestword=arr.reduce((w1,w2)=>w1.length<w2.length?w1:w2)
console.log(shortestword);

