function performAddition(){

    let num1=+document.querySelector("#box1").value

    let num2=+document.querySelector("#box2").value

    // let num1=+box1.value

    let result=num1+num2

    // console.log(result);
    document.querySelector("#root").innerHTML=`${num1}+${num2}=${result}`
}

function performSubtraction(){

    let num1=+document.querySelector("#box1").value   //let num1=+box1.value

    let num2=+document.querySelector("#box2").value

    let result=num1-num2

    // console.log(result);
    document.querySelector("#root").innerHTML=`${num1}-${num2}=${result}`
}

function performMultiplication(){

    let num1=+document.querySelector("#box1").value

    let num2=+document.querySelector("#box2").value

    let result=num1*num2

    document.querySelector("#root").innerHTML=`${num1}*${num2}=${result}`

    // console.log(result);
}

function performDivision(){

    // let num1=+document.querySelector("#box1").value

    // let num2=+document.querySelector("#box2").value

    let num1=+box1.value
    let num2=+box2.value
    let result=num1/num2
    document.querySelector("#root").innerHTML=`${num1}/${num2}=${result}`
    // console.log(result);
}

function handleClick(event){
    let operator=event.target.value;
    let num1=box1.value
    let num2=box2.value
    let result=eval(`${num1}${operator}${num2}`)
    document.querySelector("#root").innerHTML=`${num1}${operator}${num2}=${result}`
}