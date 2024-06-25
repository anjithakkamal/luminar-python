// javascript runtime
setTimeout(()=>{
    console.log("line 1");
},2000)

console.log("line 2");

setTimeout(()=>{
    console.log("line 3");
},0)

console.log("line 4");

setTimeout(()=>{
    console.log("line 5");
},1000)