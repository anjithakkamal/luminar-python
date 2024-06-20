var weight_in_kg=35

var height_in_cm=153

var height_in_meter=height_in_cm/100

var bmi=Math.round(weight_in_kg/height_in_meter**2)

console.log(`bmi ${bmi}`);

if (bmi<19){

    console.log("underweight");
}

else if(bmi<=25){

    console.log("normal");
}

else if(bmi<=30){

    console.log("over weight");
}

else{

    console.log("obese");
}