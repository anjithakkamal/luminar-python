// first recursive character
var text="ABCBDDE"
var wc={}
for(let ch of text){
    if(ch in wc){
        console.log(ch,"is first recursive charcter");
        break
    }
    else{
        wc[ch]=1
    }
}