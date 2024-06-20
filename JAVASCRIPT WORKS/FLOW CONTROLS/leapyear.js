var year=2014

if ((year%100==0 && year%400==0) || (year%100!=0 && year%4==0)){

    console.log(year,"year is leap year");
}
else{

    console.log(year,"not leap year");
}