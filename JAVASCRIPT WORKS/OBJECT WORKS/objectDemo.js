var items={potato:45,tomato:35,ginger:250,garlic:300,oninon:50}

var nestedArray=Object.entries(items)     //array of array [[],[]] nested array

console.log(nestedArray);

var costly=nestedArray.reduce((p1,p2)=>p1[1]>p2[1]?p1:p2)

console.log("costly product :",costly);
