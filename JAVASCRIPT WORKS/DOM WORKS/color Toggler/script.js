function handleClick(event){
    let color=event.target.value;
    let rootElement=document.querySelector("#root")
    rootElement.removeAttribute("class")
    rootElement.setAttribute("class",`bg-${color}`)
    // console.log(color);
}