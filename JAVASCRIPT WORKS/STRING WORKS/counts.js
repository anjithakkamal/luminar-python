var text="pneumonoultramicroscopicsilicovolcanoconiosis"
var vowels="aeiou"
var v_count=0
var c_count=0
for(let ch of text){
   
    if(vowels.includes(ch)){

        v_count++
    }
    else{
        c_count++
    }
}
console.log("vowels count",v_count);
console.log("consonent count",c_count);
console.log("total character",text.length);