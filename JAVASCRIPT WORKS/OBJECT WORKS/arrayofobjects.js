 var products=[

    {id:1,title:"samasungs23ultra",price:130000,brand:"samsung"},
    {id:2,title:"m32",price:35000,brand:"samsung"},
    {id:3,title:"opporeno",price:27000,brand:"oppo"},
    {id:4,title:"mi21note",price:23000,brand:"mi"},
    {id:5,title:"moto edge 40",price:230000,brand:"moto"},
    {id:6,title:"moto ede40 neo",price:250000,brand:"moto"},
    {id:7,title:"iphone13",price:140000,brand:"apple"},
    {id:8,title:"iphone13pro",price:150000,brand:"apple"},
  
]
// total no of products
console.log("total no of products : ",products.length);

// product names
var productNames=products.map(p=>p.title)
console.log("product names =",productNames);

// all mobiles names available under rs 35k
var mobilePriceFilter=products.filter(p=>p.price<35000).map(p=>p.title)   //method chaining
console.log("mobile price filter <35000 = ",mobilePriceFilter);

// all samsung mobile available  under 50k
var samsungMobileFilter=products.filter(p=>p.brand =="samsung" && p.price<50000).map(p=>p.title)
console.log("samsungMobileFilter = ",samsungMobileFilter);

// costly product
var costlyproduct=products.reduce((p1,p2)=>p1.price>p2.price?p1.title:p2.title)
console.log("costly product : ",costlyproduct);

// sort products wrt price order to desc
products.sort((p1,p2)=>p2.price-p1.price)
console.log("product sorted = ",products.map(p=>p.title));

// product names available in range of 25k-35k

var priceFilter=products.filter(p=>p.price>=25000 && p.price<=35000).map(p=>p.title)
console.log("pricefilter =",priceFilter);