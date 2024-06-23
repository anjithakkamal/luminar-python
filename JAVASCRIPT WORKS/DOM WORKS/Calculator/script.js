var pointfrequency=1

function displayNumber(event){

    // let num=event.target.value

    // document.querySelector("#result").value+=num

    const operators=["+","-","*","/","."]

    let textbox=document.querySelector("#result")

    // extrct current exp

    let currentExpression=textbox.value;

    // extrct disply number

    let DisplayNumber=event.target.value;

    if (DisplayNumber=="." && pointfrequency==1){

        pointfrequency=0
    }

    else if(DisplayNumber=="." && pointfrequency==0){

        return
    }

    if(operators.includes(DisplayNumber)&& DisplayNumber!="."){

        pointfrequency=1
    }

    // extrct lst char from currnt exp

    let curExpLastChar=currentExpression.slice(-1)

    // chk for dispklynum and curexplstchar are opertor

    if(operators.includes(DisplayNumber) && operators.includes(curExpLastChar)){

        currentExpression=currentExpression.slice(0,-1)
    }
    textbox.value=currentExpression+DisplayNumber

    // textbox.value=currentExpression+currentDisplayNumber
}

function ClearResult(event){

    document.querySelector("#result").value=""

}

function evaluateExpression(){

    let currentExpression=document.querySelector("#result").value

    let result=eval(currentExpression)

    

    // pointfrequency=1

    if(result.toString().split().includes('.')){

        pointfrequency=0
    }

    else{
        pointfrequency=1
    }

    document.querySelector("#result").value=result
}

function backSpace(){

    let currentElement=document.querySelector("#result").value

    let result=currentElement.slice(0,-1)

    document.querySelector("#result").value=result
}
